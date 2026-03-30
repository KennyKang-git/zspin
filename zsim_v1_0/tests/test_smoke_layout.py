from pathlib import Path


def test_base_config_exists():
    assert Path("configs/base.yaml").exists()
