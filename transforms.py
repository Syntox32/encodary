import base64
import gzip
import zlib

def t_b64encode(s: bytes) -> bytes: return base64.b64encode(s)
def t_b32encode(s: bytes) -> bytes: return base64.b32encode(s)
def t_b16encode(s: bytes) -> bytes: return base64.b16encode(s)
def t_b85encode(s: bytes) -> bytes: return base64.b85encode(s)

def t_b64encode_rev(s: bytes) -> bytes: return base64.b64encode(s)[::-1]
def t_b32encode_rev(s: bytes) -> bytes: return base64.b32encode(s)[::-1]
def t_b16encode_rev(s: bytes) -> bytes: return base64.b16encode(s)[::-1]
def t_b85encode_rev(s: bytes) -> bytes: return base64.b85encode(s)[::-1]

def t_rev_b64encode(s: bytes) -> bytes: return base64.b64encode(s[::-1])
def t_rev_b32encode(s: bytes) -> bytes: return base64.b32encode(s[::-1])
def t_rev_b16encode(s: bytes) -> bytes: return base64.b16encode(s[::-1])
def t_rev_b85encode(s: bytes) -> bytes: return base64.b85encode(s[::-1])

def t_gzip(s: bytes) -> bytes: return gzip.compress(s)

def t_gzip_b64(s: bytes) -> bytes: return base64.b64encode(gzip.compress(s))
def t_gzip_b32(s: bytes) -> bytes: return base64.b32encode(gzip.compress(s))
def t_gzip_b16(s: bytes) -> bytes: return base64.b16encode(gzip.compress(s))
def t_gzip_b85(s: bytes) -> bytes: return base64.b85encode(gzip.compress(s))

def t_zlib_b64(s: bytes) -> bytes: return base64.b64encode(zlib.compress(s)) #[:3]
def t_zlib_b32(s: bytes) -> bytes: return base64.b32encode(zlib.compress(s)) #[:3]
def t_zlib_b16(s: bytes) -> bytes: return base64.b16encode(zlib.compress(s)) #[:3]
def t_zlib_b85(s: bytes) -> bytes: return base64.b85encode(zlib.compress(s)) #[:3]