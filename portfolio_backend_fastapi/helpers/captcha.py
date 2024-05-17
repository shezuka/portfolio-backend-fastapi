import logging

import httpx
from fastapi import HTTPException

from portfolio_backend_fastapi.config import RECAPTCHA_SECRET_KEY, RECAPTCHA_API_KEY, GOOGLE_PROJECT_ID

logger = logging.getLogger(__name__)


async def assert_captcha(captcha_token: str, expected_action: str):
    """
    Verifies a captcha token.
    :param captcha_token: The captcha token to verify.
    :param expected_action: The expected action of the captcha token.
    :return: True if the captcha token is valid, False otherwise.
    """

    payload = {
        "event": {
            "token": captcha_token,
            "expectedAction": expected_action,
            "siteKey": RECAPTCHA_SECRET_KEY,
        }
    }
    url = f"https://recaptchaenterprise.googleapis.com/v1/projects/{GOOGLE_PROJECT_ID}/assessments?key={RECAPTCHA_API_KEY}"

    async with httpx.AsyncClient() as client:
        logger.error(f"Sending captcha token to reCAPTCHA: {url}")
        response = await client.post(url, json=payload)
        result = response.json()
        if response.status_code != 200 or not result.get("tokenProperties", {}).get("valid", False):
            logger.error(f"Invalid captcha token: {result}")
            raise HTTPException(status_code=400, detail="Invalid CAPTCHA")

        if result.get("riskAnalysis", {}).get("score", 0) < 0.5:  # Adjust score threshold as needed
            raise HTTPException(status_code=400, detail="Low reCAPTCHA score")
