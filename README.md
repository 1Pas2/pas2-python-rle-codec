# pas2-python-rle-codec

Encode binary runs with bounded decompression.

Part of **Pas2 Polyglot** by [1Pas2](https://github.com/1Pas2): independent small projects in PHP, Python, Go and C#. No runtime dependencies outside the language standard library. Initial version: 0.1.0.

## Requirements and installation

Python 3.11+. Install a checkout using `python -m pip install .`. The import name is `pas2_rle_codec`. PyPI publication was not performed.

## Example

```python
import pas2_rle_codec as api

encoded = api.encode(b"aaaaabbbcc")
print(encoded, api.decode(encoded))
```

## API and limits

encode(bytes) emits pairs of one-byte count (1..255) and byte value. decode(bytes,max_output=1000000) validates the entire output size before allocating. There is no file header, checksum, streaming interface or automatic format detection; high-entropy input can expand.

## Tests and example

From the repository root:

```sh
python -m pip install -e .
python -m unittest discover -s tests -v
python examples/basic.py
```

Tests use the standard library or a dependency-free executable check harness. A failing assertion exits nonzero. The example is self-contained and uses local in-memory or temporary data. CI runs the same checks on Linux. No registry releases, downloads, users or production deployments are claimed.

## Contributing

Open a focused issue or pull request with reproduction steps and a behavioral test. Run the commands above before submitting. Do not include credentials or private data in reports.

## Ecosystem

[Browse Pas2 projects](https://github.com/1Pas2?tab=repositories&q=pas2-). Each repository is usable independently. The earlier TypeScript series and this polyglot series have distinct repository names.

## License

[MIT](LICENSE) © 2026 1Pas2.

1Pas2
