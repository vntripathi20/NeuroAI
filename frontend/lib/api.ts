const API_URL = process.env.NEXT_PUBLIC_API_URL ?? "http://localhost:8000";

export interface HealthResponse {
  status: string;
  service: string;
}

export async function getBackendHealth(): Promise<HealthResponse> {
  const response = await fetch(`${API_URL}/health`, { cache: "no-store" });

  if (!response.ok) {
    throw new Error(`Backend health check failed with status ${response.status}`);
  }

  return response.json() as Promise<HealthResponse>;
}
