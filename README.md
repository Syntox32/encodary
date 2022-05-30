# encodary.py

A script for generating rainbow tables for simple encodings and string transformations.

Running this will create the canaries:
```
python3 generate_canaries.py
```

This creates three new files in this the same directory:

  * `canary.lst`: All canaries in a simple list form.
  * `lookup.lst`: A simple lookup with the transform, canary, and the common word used to create it.
  * `canary.json`: A lookup formatted as JSON file.