#!/usr/bin/env python3
"""
Validation script for academic domain authority scoring.
Tests that academic domains are correctly loaded and scored.
"""

import json
import sys
from pathlib import Path

# Add search.py path for imports
sys.path.insert(0, str(Path(__file__).parent))

from search import _load_authority_data, get_authority_score

# Test domains with expected scores
ACADEMIC_TEST_CASES = [
    # Tier 1 Academic (score: 1.0)
    ("https://www.nature.com/articles/s41586-025-00001-2", 1.0, "Nature - Tier 1 Academic"),
    ("https://www.sciencemag.org/doi/10.1126/science.abc123", 1.0, "Science - Tier 1 Academic"),
    ("https://www.cell.com/cell/fulltext/S0092-8674(25)001234", 1.0, "Cell Press - Tier 1 Academic"),
    ("https://arxiv.org/abs/2501.12345", 1.0, "arXiv - Tier 1 Academic"),
    ("https://www.biorxiv.org/content/10.1101/2025.01.01.123456", 1.0, "bioRxiv - Tier 1 Academic"),
    ("https://chemrxiv.org/engage/api/v1/works/abc123", 1.0, "chemRxiv - Tier 1 Academic"),
    ("https://pubmed.ncbi.nlm.nih.gov/12345678/", 1.0, "PubMed - Tier 1 Academic"),
    ("https://www.ncbi.nlm.nih.gov/pmc/articles/PMC1234567/", 1.0, "NCBI/PMC - Tier 1 Academic"),

    # Tier 2 Academic (score: 0.8)
    ("https://ieeexplore.ieee.org/document/12345678", 0.8, "IEEE Xplore - Tier 2 Academic"),
    ("https://www.ieee.org/publications/standards.html", 0.8, "IEEE.org - Tier 2 Academic"),
    ("https://dl.acm.org/doi/10.1145/1234567.1234568", 0.8, "ACM DL - Tier 2 Academic"),
    ("https://www.acm.org/publications", 0.8, "ACM.org - Tier 2 Academic"),
    ("https://link.springer.com/article/10.1007/s12345-025-6789", 0.8, "Springer Link - Tier 2 Academic"),
    ("https://www.springer.com/gp", 0.8, "Springer.com - Tier 2 Academic"),
    ("https://www.sciencedirect.com/science/article/pii/S1234567825001234", 0.8, "ScienceDirect - Tier 2 Academic"),
    ("https://onlinelibrary.wiley.com/doi/10.1002/xyz.12345", 0.8, "Wiley Online - Tier 2 Academic"),
    ("https://pubs.acs.org/doi/10.1021/jacs.5c12345", 0.8, "ACS Publications - Tier 2 Academic"),
    ("https://iopscience.iop.org/article/10.1088/1234-5678/abc1234", 0.8, "IOP Publishing - Tier 2 Academic"),
    ("https://pubs.rsc.org/en/content/articlelanding/2025/cs/d123456", 0.8, "RSC Publishing - Tier 2 Academic"),
    ("https://osf.io/preprints/12345", 0.8, "OSF Preprints - Tier 2 Academic"),

    # Tier 3 Academic (score: 0.6)
    ("https://scholar.google.com/scholar?q=machine+learning", 0.6, "Google Scholar - Tier 3 Academic"),
    ("https://www.researchgate.net/publication/12345678", 0.6, "ResearchGate - Tier 3 Academic"),
    ("https://www.academia.edu/12345678", 0.6, "Academia.edu - Tier 3 Academic"),
    ("https://www.mdpi.com/1234-5678/25/1/123", 0.6, "MDPI - Tier 3 Academic"),
    ("https://www.frontiersin.org/articles/10.3389/f12345", 0.6, "Frontiers - Tier 3 Academic"),
    ("https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0123456", 0.6, "PLOS - Tier 3 Academic"),

    # Tier 4 Academic (score: 0.4)
    ("https://www.deepdyve.com/document/12345", 0.4, "DeepDyve - Tier 4 Academic"),

    # Existing non-academic domains for baseline
    ("https://github.com/user/repo", 1.0, "GitHub - Tier 1 General"),
    ("https://stackoverflow.com/questions/123", 1.0, "Stack Overflow - Tier 1 General"),
    ("https://dev.to/somepost", 0.8, "dev.to - Tier 2 General"),
    ("https://medium.com/article", 0.6, "Medium - Tier 3 General"),
]

# Additional edge cases
EDGE_CASES = [
    ("https://subdomain.nature.com/article", 1.0, "Nature subdomain"),
    ("https://www.biorxiv.org/content/early/2025/01/01", 1.0, "bioRxiv early view"),
    ("https://ieeexplore.ieee.org", 0.8, "IEEE Xplore main domain"),
    ("https://dl.acm.org", 0.8, "ACM DL main domain"),
    ("https://unknown.edu.cn/something", 0.8, "Unknown .edu domain (pattern rule)"),
    ("https://nih.gov", 0.8, "NIH .gov domain (pattern rule)"),
    ("https://fake-university.edu", 0.8, "Fake .edu domain (pattern rule)"),
]


def run_tests():
    """Run all validation tests."""
    print("=" * 70)
    print("Academic Domain Authority Scoring - Validation Tests")
    print("=" * 70)

    # Load authority data
    print("\n[1] Loading authority data...")
    domain_scores, pattern_rules, default_score = _load_authority_data()
    print(f"    Loaded {len(domain_scores)} domains")
    print(f"    Loaded {len(pattern_rules)} pattern rules")
    print(f"    Default score: {default_score}")

    # Check academic domains loaded
    academic_domains = [d for d in domain_scores.keys() if d in [
        "nature.com", "sciencemag.org", "cell.com", "arxiv.org",
        "biorxiv.org", "chemrxiv.org", "ncbi.nlm.nih.gov",
        "ieee.org", "ieeexplore.ieee.org", "acm.org", "dl.acm.org",
        "springer.com", "link.springer.com", "sciencedirect.com",
        "onlinelibrary.wiley.com", "pubs.acs.org", "iop.org", "pubs.rsc.org",
        "osf.io", "researchgate.net", "academia.edu", "mdpi.com",
        "frontiersin.org", "plos.org", "deepdyve.com", "scholar.google.com"
    ]]
    print(f"    Academic domains loaded: {len(academic_domains)}")

    # Run main test cases
    print("\n[2] Testing academic domain scoring...")
    passed = 0
    failed = 0

    for url, expected, description in ACADEMIC_TEST_CASES:
        actual = get_authority_score(url)
        status = "✓" if abs(actual - expected) < 0.01 else "✗"
        if status == "✓":
            passed += 1
        else:
            failed += 1
        print(f"    {status} {description}: {url[:50]}...")
        if status == "✗":
            print(f"         Expected: {expected}, Got: {actual}")

    # Run edge cases
    print("\n[3] Testing edge cases...")
    for url, expected, description in EDGE_CASES:
        actual = get_authority_score(url)
        status = "✓" if abs(actual - expected) < 0.01 else "○"
        print(f"    {status} {description}: {url[:50]}...")
        print(f"         Expected: {expected}, Got: {actual}")

    # Summary
    print("\n" + "=" * 70)
    print("Test Summary")
    print("=" * 70)
    print(f"    Total tests: {len(ACADEMIC_TEST_CASES)}")
    print(f"    Passed: {passed}")
    print(f"    Failed: {failed}")

    if failed == 0:
        print("\n✓ All academic domain scoring tests PASSED!")
        return 0
    else:
        print(f"\n✗ {failed} tests FAILED!")
        return 1


def test_json_schema():
    """Validate authority-domains.json schema."""
    print("\n[4] Validating authority-domains.json schema...")

    ref_path = Path(__file__).parent.parent / "references" / "authority-domains.json"

    try:
        with open(ref_path) as f:
            data = json.load(f)

        # Check required fields
        required_tiers = ["tier1", "tier2", "tier3"]
        for tier in required_tiers:
            if tier not in data:
                print(f"    ✗ Missing required tier: {tier}")
                return 1
            if "domains" not in data[tier]:
                print(f"    ✗ Missing 'domains' in {tier}")
                return 1
            if "score" not in data[tier]:
                print(f"    ✗ Missing 'score' in {tier}")
                return 1

        # Check academic section
        if "academic" in data:
            academic_tiers = ["tier1_academic", "tier2_academic", "tier3_academic", "tier4_academic"]
            for tier in academic_tiers:
                if tier in data["academic"]:
                    if "domains" not in data["academic"][tier]:
                        print(f"    ✗ Missing 'domains' in academic.{tier}")
                        return 1
                    if "score" not in data["academic"][tier]:
                        print(f"    ✗ Missing 'score' in academic.{tier}")
                        return 1

        # Check pattern_rules
        if "pattern_rules" not in data:
            print(f"    ✗ Missing 'pattern_rules'")
            return 1

        print(f"    ✓ JSON schema is valid")
        print(f"    ✓ Contains {len(data.get('tier1', {}).get('domains', []))} tier1 domains")
        print(f"    ✓ Contains {len(data.get('tier2', {}).get('domains', []))} tier2 domains")
        print(f"    ✓ Contains {len(data.get('tier3', {}).get('domains', []))} tier3 domains")
        if "academic" in data:
            ac_domains = sum(len(data["academic"].get(t, {}).get("domains", []))
                           for t in ["tier1_academic", "tier2_academic", "tier3_academic", "tier4_academic"])
            print(f"    ✓ Contains {ac_domains} academic domains")

        return 0

    except json.JSONDecodeError as e:
        print(f"    ✗ Invalid JSON: {e}")
        return 1
    except Exception as e:
        print(f"    ✗ Error: {e}")
        return 1


if __name__ == "__main__":
    ret1 = run_tests()
    ret2 = test_json_schema()

    sys.exit(ret1 or ret2)
