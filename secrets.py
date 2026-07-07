# Must be EXCLUDED everywhere by this root .blitzyignore rule ("secrets.py"),
# including inside every submodule (root patterns are unanchored -- unchanged
# behavior, not part of the ABK-4487 fix).
API_KEY = "should-never-be-onboarded"
