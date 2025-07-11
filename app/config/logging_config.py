import logging

logger = logging.getLogger("pricing_rules")
logger.setLevel(logging.INFO)

# Formato del log
formatter = logging.Formatter(
    "[%(asctime)s] %(levelname)s - %(name)s - %(message)s", "%Y-%m-%d %H:%M:%S"
)

# Consola
console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)

# Evita múltiples handlers si ya están configurados
if not logger.handlers:
    logger.addHandler(console_handler)
