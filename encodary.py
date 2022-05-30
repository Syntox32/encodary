import json
from importlib import import_module as im


def longest_common_string(s1: str, s2: str) -> str:
  for idx, (c1, c2) in enumerate(zip(s1, s2)):
    if c1 != c2:
      break
  return s1[:idx]

def clean(s: str) -> str:
  return s.replace("\n", "").replace("\r", "")

if __name__ == "__main__":
  with open("canaries.txt", "r", encoding="utf-8") as canaries:
    cc = [clean(c) for c in canaries.readlines()]

  transforms = im("transforms")
  functions = [func_name for func_name in dir(transforms) if func_name.startswith("t_")]
  gen = []
  lookup = []
  generated_file = {}
  ignore_length = 4  # if the common_s is not longer than 4 characters it will be ignored

  for func_name in functions:
      f = getattr(transforms, func_name)
      for canary in cc:
        try:
          # remove padding (==) because we look for encoding other strings
          s1 = f(canary.encode("utf-8")).decode("utf-8").replace("=", "")

          s2 = ""
          if func_name.startswith("t_rev"):
            s2 = f(("A"*32 + canary).encode("utf-8")).decode("utf-8").replace("=", "")
          else:
            s2 = f((canary + "A"*32).encode("utf-8")).decode("utf-8").replace("=", "")

          common_s = ""
          if func_name.endswith("_rev"):
            common_s = longest_common_string(s1[::-1], s2[::-1])[::-1]
          else:
            common_s = longest_common_string(s1, s2)

          if len(common_s) >= ignore_length:
            log = f"{func_name}: {canary} -> {common_s}"
            print(log)
            gen.append(common_s)
            lookup.append(log)
            generated_file[common_s] = dict(identifier=canary, transform=func_name)

        except Exception as e:
          print(func_name)

  with open("canary.lst", "w", encoding="utf-8") as f:
    f.write("\n".join(gen))

  with open("lookup.lst", "w", encoding="utf-8") as f:
    f.write("\n".join(lookup))

  with open("canary.json", "w", encoding="utf-8") as f:
    f.write(json.dumps(generated_file, indent=4))

  print(f"Generated {len(gen)} variations")
  print(f"Generated {len(set(gen))} unique variations")