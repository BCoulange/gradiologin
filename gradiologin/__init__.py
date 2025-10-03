from gradiologin.functions import get_user, LogoutButton
from gradiologin.register import register, mount_gradio_app
import logging

logger = logging.getLogger(__name__)  # NOT root

# usage
logger.info("Starting login flow")
