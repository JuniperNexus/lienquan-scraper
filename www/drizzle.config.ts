import dotenvx from "@dotenvx/dotenvx"
import { defineConfig } from "drizzle-kit"

export default defineConfig({
  out: "./src/server/db",
  schema: "./src/server/db/schema.ts",
  dialect: "sqlite",
  dbCredentials: {
    url: dotenvx.get("DATABASE_FILENAME"),
  },
})
