import pas2_rle_codec as api

encoded = api.encode(b"aaaaabbbcc")
print(encoded, api.decode(encoded))
