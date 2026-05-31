"""
Tests for ΦCyberBot Security
"""

import pytest
from phicyberbot_security import PhiCyberBotSecurity


@pytest.fixture
def system():
    """Create system instance for tests"""
    return PhiCyberBotSecurity()


def test_initialization(system):
    """Test system initialization"""
    assert system.version == "2.0.0"
    assert system.status == "Production Ready"


def test_process(system):
    """Test process function"""
    result = system.process({"test": "input"})
    
    assert result["status"] == "success"
    assert result["project"] == "ΦCyberBot Security"
    assert result["version"] == "2.0.0"


def test_info(system):
    """Test get_info function"""
    info = system.get_info()
    
    assert info["name"] == "ΦCyberBot Security"
    assert info["version"] == "2.0.0"
    assert info["type"] == "security"


@pytest.mark.asyncio
async def test_async_process(system):
    """Test async process"""
    result = await system.process_async({"test": "async"})
    assert result["status"] == "success"
