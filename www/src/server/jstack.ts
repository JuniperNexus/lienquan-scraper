import Database from "better-sqlite3"
import { drizzle } from "drizzle-orm/better-sqlite3"
import { env } from "hono/adapter"
import { jstack } from "jstack"

type Env = {
  Bindings: {
    DATABASE_FILENAME: string
  }
}

export const j = jstack.init<Env>()

/**
 * Type-safely injects database into all procedures
 *
 * @see https://jstack.app/docs/backend/middleware
 */
const databaseMiddleware = j.middleware(async ({ c, next }) => {
  const { DATABASE_FILENAME } = env(c)

  const sqlite = new Database(DATABASE_FILENAME)
  const db = drizzle(sqlite)

  return await next({ db })
})

/**
 * Public (unauthenticated) procedures
 *
 * This is the base piece you use to build new queries and mutations on your API.
 */
export const publicProcedure = j.procedure.use(databaseMiddleware)
