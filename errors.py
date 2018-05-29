import raven
import os

SENTRY_DSN = os.environ.get('SENTRY_DSN')

client = raven.Client(SENTRY_DSN,
		 release=raven.fetch_git_sha(os.path.dirname(__file__)),
	)

try:
    1 / 0
except ZeroDivisionError:
    client.captureException()