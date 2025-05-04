import { heroes } from "@/server/db/schema"
import { j, publicProcedure } from "@/server/jstack"
import { desc } from "drizzle-orm"

export const heroesRouter = j.router({
  list: publicProcedure.query(async ({ c, ctx }) => {
    const { db } = ctx

    try {
      const list = await db.select().from(heroes).orderBy(desc(heroes.id))

      return c.superjson(list)
    } catch (error) {
      console.error(error)
      throw new Error("Failed to fetch heroes", { cause: error })
    }
  }),
})
