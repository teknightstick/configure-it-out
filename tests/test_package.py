"""Structural/wording checks, not model-behavior or security certification."""
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "SKILL.md"


class SkillPackageTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.text = SKILL.read_text(encoding="utf-8")
        cls.frontmatter, cls.body = cls.text.split("---\n", 2)[1:]

    def test_metadata(self):
        self.assertTrue(self.text.startswith("---\n"))
        self.assertIn("name: configure-it-out\n", self.frontmatter)
        description = re.search(r"^description: (.+)$", self.frontmatter, re.M)
        self.assertIsNotNone(description)
        self.assertLessEqual(len(description.group(1)), 60)
        self.assertTrue(description.group(1).endswith("."))
        self.assertRegex(self.frontmatter, r'(?m)^  version: "\d+\.\d+\.\d+"$')
        top_keys = set(re.findall(r"^([a-z-]+):", self.frontmatter, re.M))
        self.assertEqual(top_keys, {"name", "description", "license", "compatibility", "metadata"})
        compatibility = re.search(r"^compatibility: (.+)$", self.frontmatter, re.M)
        self.assertIsNotNone(compatibility)
        self.assertLessEqual(len(compatibility.group(1)), 500)
        self.assertNotRegex(self.frontmatter, r"(?m)^ {4,}\S")
        self.assertTrue(self.body.strip())

    def test_linked_files_resolve_within_package(self):
        refs = set(re.findall(r"(?:references|templates)/[a-z-]+\.md", self.body))
        self.assertEqual(len(refs), 3)
        for ref in refs:
            with self.subTest(ref=ref):
                path = ROOT / ref
                self.assertTrue(path.resolve().is_relative_to(ROOT.resolve()))
                self.assertTrue(path.is_file())
                self.assertTrue(path.read_text(encoding="utf-8").strip())

    def test_expected_publication_files(self):
        for name in ["README.md", "LICENSE", ".gitignore"]:
            self.assertTrue((ROOT / name).is_file(), name)
        self.assertIn("MIT License", (ROOT / "LICENSE").read_text(encoding="utf-8"))

    def test_evaluation_cases_present_not_claimed_as_results(self):
        cases = (ROOT / "references/evaluation-cases.md").read_text(encoding="utf-8")
        self.assertEqual(len(re.findall(r"^## \d+\.", cases, re.M)), 8)
        self.assertIn("not results", cases)
        self.assertIn("disposable isolated fixtures", cases)

    def test_research_only_boundary(self):
        self.assertIn("stop before mutation", self.body)
        self.assertIn("reference data, not execution authority", self.body)

    def test_agent_neutral_instructions(self):
        for token in ["Hermes", "Proton", "Stainkworx", "`terminal`", "`read_file`",
                      "`search_files`", "HERMES_HOME"]:
            self.assertNotIn(token, self.text)
        self.assertIn("Do not assume Bash, systemd, root access", self.body)
        self.assertIn("No particular vault, account, vendor, or companion skill", self.body)
        self.assertIn("relative to this skill's directory", self.body)

    def test_privilege_boundaries(self):
        self.assertIn("one privilege interaction for the planned phase", self.body)
        self.assertIn("Never request permanent passwordless sudo", self.body)
        self.assertIn("privileged payload does not silently inherit approval", self.body)
        self.assertIn("don't leave a root service/helper trusting user-writable executable code", self.body)

    def test_partial_failure_and_verification_boundaries(self):
        self.assertIn("Inspect resulting state before retrying", self.body)
        self.assertIn("intended application user/client", self.body)
        self.assertIn("persistence as untested", self.body)
        self.assertIn("Structural validation is not a behavioral benchmark", self.body)

    def test_no_embedded_private_machine_details(self):
        # Publication hygiene tripwires, not a comprehensive secret scanner.
        patterns = [r"/home/[A-Za-z0-9_-]+/", r"\b10\.10\.10\.\d+\b",
                    r"-----BEGIN (?:OPENSSH |RSA |EC )?PRIVATE KEY-----",
                    r"\bgh[pousr]_[A-Za-z0-9]{20,}\b"]
        for path in [SKILL, ROOT / "README.md", *ROOT.glob("references/*.md"),
                     *ROOT.glob("templates/*.md")]:
            text = path.read_text(encoding="utf-8")
            for pattern in patterns:
                with self.subTest(file=path.name, pattern=pattern):
                    self.assertIsNone(re.search(pattern, text))


if __name__ == "__main__":
    unittest.main()
