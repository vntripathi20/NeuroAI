"use client";

import { useEffect, useState } from "react";

import { getBackendHealth, type HealthResponse } from "@/lib/api";

type ConnectionState =
  | { status: "loading" }
  | { status: "connected"; data: HealthResponse }
  | { status: "error"; message: string };

export default function Home() {
  const [connection, setConnection] = useState<ConnectionState>({ status: "loading" });

  useEffect(() => {
    getBackendHealth()
      .then((data) => setConnection({ status: "connected", data }))
      .catch((error: unknown) =>
        setConnection({
          status: "error",
          message: error instanceof Error ? error.message : "Unknown error",
        }),
      );
  }, []);

  return (
    <main className="flex min-h-screen flex-col items-center justify-center gap-6 bg-zinc-50 px-6 font-sans dark:bg-black">
      <div className="w-full max-w-md rounded-lg border border-zinc-200 bg-white p-8 dark:border-zinc-800 dark:bg-zinc-900">
        <h1 className="text-xl font-semibold text-zinc-900 dark:text-zinc-50">NeuroAI</h1>
        <p className="mt-1 text-sm text-zinc-500 dark:text-zinc-400">
          Development scaffold — frontend / backend connectivity check.
        </p>

        <div className="mt-6 rounded-md bg-zinc-50 p-4 text-sm dark:bg-zinc-800">
          {connection.status === "loading" && (
            <p className="text-zinc-500 dark:text-zinc-400">Checking backend connection…</p>
          )}
          {connection.status === "connected" && (
            <p className="text-green-700 dark:text-green-400">
              ✓ Connected to <code>{connection.data.service}</code> (status: {connection.data.status})
            </p>
          )}
          {connection.status === "error" && (
            <div className="text-red-700 dark:text-red-400">
              <p>✗ Could not reach the backend.</p>
              <p className="mt-1 text-xs text-zinc-500 dark:text-zinc-400">
                {connection.message}. Is the FastAPI server running on the configured
                NEXT_PUBLIC_API_URL?
              </p>
            </div>
          )}
        </div>
      </div>
    </main>
  );
}
