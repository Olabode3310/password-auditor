# Offline Password Auditing & Hash Analysis Toolkit

A command line utility for estimating password strength and checking supplied password hashes against a small local candidate list. It operates offline: there are no network calls, credential login attempts, or remote lookups. Use only hashes you are authorized to audit.

## Features

- Verification helpers for MD5, SHA-1, SHA-256, NTLM, and bcrypt.
- Transparent strength estimate using length, character classes, common-password and keyboard-walk indicators.
- Offline dictionary candidates with capitalization, simple leet substitutions, common suffixes, and years.
- Optional multiprocessing (up to eight workers) and JSON audit reports.

## Installation

Python 3.10+.

```sh
python -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt
python main.py --help
```

PyCryptodome supplies MD4 for NTLM verification; bcrypt supports bcrypt-format hashes.

## Usage

```sh
python main.py strength 'correct horse battery staple'
python main.py audit --hash-type sha256 --hash-file example_hashes.txt --wordlist wordlists/sample.txt --workers 2 --output reports/audit.json
```

Example report excerpt when the bundled SHA-256 fixture matches the sample wordlist:

```json
{
  "hash_type": "sha256",
  "hashes_checked": 1,
  "elapsed_seconds": 0.01,
  "results": [{"status": "cracked", "password": "winter", "strength": {"score_0_to_4": 0}}]
}
```

## Project Structure

```text
hashers/          Hash verification functions
attackers/        Offline dictionary and candidate mutations
strength/         Heuristic strength estimate
wordlists/        Small demonstration list
reports/          Report destination
example_hashes.txt
main.py
```

## Legal & Ethical Use

This toolkit is strictly for offline auditing of password hashes that you own or have explicit written authorization to assess. Confirm the approved dataset and purpose before handling any credential material. Never use recovered passwords to authenticate to accounts, test live services, or access systems. Hashes and recovered passwords are highly sensitive: restrict access, avoid publishing real credentials or reports, store data only in approved locations, and securely delete working copies when the audit is complete. Do not commit real hashes, wordlists obtained from restricted sources, or recovered passwords to a public repository. Unauthorized password auditing or use of recovered credentials may violate law, contracts, and organizational policy.

## Limitations

Entropy is a rough estimate and does not model language, reuse, or modern password cracking hardware. Dictionary coverage is intentionally tiny. The mutation set is basic and can miss many candidates. Multiprocessing overhead can outweigh benefits for small wordlists. Bcrypt hashes can use different cost settings, so verification speed depends on the supplied hash. NTLM requires PyCryptodome. This tool does not provide a reliable time-to-crack prediction; hardware and attacker strategy vary too widely for a useful fixed estimate.

## Tests

`python -m unittest discover -s tests -v`
