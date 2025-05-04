import { cors } from "hono/cors"

import { j } from "./jstack"
import { heroesRouter } from "./routers/heroes"

/**
 * This is your base API.
 * Here, you can handle errors, not-found responses, cors and more.
 *
 * @see https://jstack.app/docs/backend/app-router
 */
const api = j
  .router()
  .basePath("/api")
  .use(
    cors({
      allowHeaders: ["x-is-superjson", "content-type"],
      exposeHeaders: ["x-is-superjson"],
      origin: ["http://localhost:3000"],
      credentials: true,
    }),
  )
  .onError(j.defaults.errorHandler)

/**
 * This is the main router for your server.
 * All routers in /server/routers should be added here manually.
 */
const appRouter = j.mergeRouters(api, {
  heroes: heroesRouter,
})

export type AppRouter = typeof appRouter

export default appRouter
