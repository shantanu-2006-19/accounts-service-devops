"""
Application Package Initialization
"""
import sys
from flask import Flask
from flask_cors import CORS
from flask_talisman import Talisman
from service.common import log_handlers

# Create the Flask application
app = Flask(__name__)

# Load configuration settings
app.config.from_object("service.config")

# Set up Cross-Origin Resource Sharing (CORS)
CORS(app)

# Set up Talisman security headers
Talisman(
    app,
    content_security_policy=None,
    force_https=False
)

# Set up logging for production
log_handlers.init_app(app)

app.logger.info(70 * "*")
app.logger.info("  A C C O U N T   S E R V I C E   R U N N I N G  ".center(70, "*"))
app.logger.info(70 * "*")

try:
    # Import routes after application is created
    from service import routes, models
except Exception as error:
    app.logger.critical("%s: Cannot continue", error)
    sys.exit(4)

app.logger.info("Service initialized successfully.")
