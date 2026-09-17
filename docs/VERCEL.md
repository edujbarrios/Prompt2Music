# Deploy Prompt2Music on Vercel

Prompt2Music can run as a full-stack Reflex application on Vercel using Vercel's container runtime.

Vercel automatically detects `Dockerfile.vercel`, builds the image, stores it in Vercel Container Registry, and runs it on Fluid Compute.

## Architecture

```text
Browser
  |
  | HTTPS / WebSocket
  v
Vercel Fluid Compute
  |
  v
Caddy :$PORT
  |-- static frontend -> /srv
  `-- Reflex backend routes -> localhost:8000
                              |
                              v
             text-to-music-prompt-structurer
```

`text-to-music-prompt-structurer` is the backend / structuring engine used by Prompt2Music. It is an open-source Python library created and maintained by Eduardo J. Barrios (@edujbarrios).

## Import the repository

1. Create a new Vercel project.
2. Import `edujbarrios/Prompt2Music` from GitHub.
3. Leave the project root at the repository root.
4. Vercel should detect `Dockerfile.vercel` as a container deployment.
5. Deploy.

No external AI API key is required.

## Runtime

Vercel provides the public `$PORT` used by `Caddyfile.vercel`.

Caddy serves the pre-built Reflex frontend and proxies Reflex backend endpoints, including the event WebSocket, to port `8000` inside the same container.

The Reflex backend runs with `GRANIAN_WORKERS=1`. Prompt2Music does not persist conversations, so the first public deployment does not require a database or external Redis instance.

## Preview deployments

When the Vercel project is connected to this GitHub repository, Vercel creates preview deployments for branches and pull requests and updates production from the configured production branch (normally `main`).

The app intentionally does not hard-code a Vercel hostname. Reflex uses the current HTTPS origin for its backend connection, so preview and production URLs can both use the same image.

## Local container check

Build the Vercel image locally:

```bash
docker build -f Dockerfile.vercel -t prompt2music-vercel .
```

Run it on port 8080:

```bash
docker run --rm -e PORT=8080 -p 8080:8080 prompt2music-vercel
```

Then open `http://localhost:8080`.

## Health endpoint

The Reflex health endpoint is available at:

```text
/_health
```

Caddy proxies it to the Reflex backend.

## Scaling note

Prompt2Music currently keeps conversation state ephemeral and in memory. A user's active Reflex WebSocket remains attached to the running container handling that connection. If persistent conversations or cross-instance state are introduced later, add a managed Redis-compatible store rather than writing state to the container filesystem.
