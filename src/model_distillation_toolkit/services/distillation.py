from __future__ import annotations

import logging
from typing import Any, Dict

logger = logging.getLogger(__name__)


class DistillationService:
    """Domain service for Model distillation toolkit."""

    def __init__(self, model_name: str = "dummy") -> None:
        self.model_name = model_name

    async def run(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        logger.info("running distillation service", extra={"keys": list(payload.keys())})
        return {"ok": True, "model": self.model_name, "received": list(payload.keys())}
