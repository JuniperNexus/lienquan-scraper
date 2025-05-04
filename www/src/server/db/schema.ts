import { sqliteTable, integer, text } from "drizzle-orm/sqlite-core"

export const heroes = sqliteTable("heroes", {
  id: integer().primaryKey(),
  name: text(),
  imageUrl: text("image_url"),
})

export const skins = sqliteTable("skins", {
  id: integer().primaryKey(),
  heroId: integer("hero_id").references(() => heroes.id, { onDelete: "cascade" }),
  skinImageUrl: text("skin_image_url"),
})
