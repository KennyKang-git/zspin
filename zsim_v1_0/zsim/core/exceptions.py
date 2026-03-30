"""Custom exceptions for Z-Sim core modules."""

from __future__ import annotations


class ZSimError(Exception):
    """Base exception for Z-Sim errors."""


class StateValidationError(ZSimError, ValueError):
    """Raised when a ``ZSimState`` fails structural or numerical validation."""


class StateSerializationError(ZSimError, ValueError):
    """Raised when a state cannot be serialized or reconstructed safely."""


class ConfigValidationError(ZSimError, ValueError):
    """Raised when a config violates structural or numerical requirements."""


class ConfigLoadError(ZSimError, OSError):
    """Raised when a config file cannot be loaded or parsed."""


class IntegrationError(ZSimError, RuntimeError):
    """Raised when the reduced numerical integration loop cannot complete."""
