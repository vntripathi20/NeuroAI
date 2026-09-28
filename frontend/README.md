# NeuroAI Frontend

Next.js (App Router) + TypeScript + Tailwind frontend for the NeuroAI
project. Currently contains a single status page that verifies
connectivity to the FastAPI backend — see the root [README](../README.md)
for full project context and run instructions.

## Local development

```bash
npm install
cp .env.local.example .env.local
npm run dev
```

Requires the backend running (see root README) for the status check on
`/` to report "Connected".

## Scripts

- `npm run dev` — start the development server
- `npm run build` — production build (also type-checks and lints)
- `npm run lint` — ESLint
