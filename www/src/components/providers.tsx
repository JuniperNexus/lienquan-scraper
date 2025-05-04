"use client"

import type { PropsWithChildren } from "react"

import { Toaster } from "@/components/ui/sonner"
import { QueryCache, QueryClient, QueryClientProvider } from "@tanstack/react-query"
import { HTTPException } from "hono/http-exception"
import { useState } from "react"
import { Provider as WrapBalancerProvider } from "react-wrap-balancer"

export const Providers = ({ children }: PropsWithChildren) => {
  const [queryClient] = useState(
    () =>
      new QueryClient({
        queryCache: new QueryCache({
          onError: (err) => {
            if (err instanceof HTTPException) {
              // global error handling, e.g. toast notification ...
            }
          },
        }),
      }),
  )

  return (
    <QueryClientProvider client={queryClient}>
      <WrapBalancerProvider>{children}</WrapBalancerProvider>
      <Toaster />
    </QueryClientProvider>
  )
}
