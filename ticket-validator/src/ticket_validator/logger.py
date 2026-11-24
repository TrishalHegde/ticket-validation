
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filename="ticket_validator.log",
    filemode="a"
)

logger = logging.getLogger(__name__)
