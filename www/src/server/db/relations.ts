import { relations } from "drizzle-orm/relations"

import { heroes, skins } from "./schema"

export const skinsRelations = relations(skins, ({ one }) => ({
  hero: one(heroes, {
    fields: [skins.heroId],
    references: [heroes.id],
  }),
}))

export const heroesRelations = relations(heroes, ({ many }) => ({
  skins: many(skins),
}))
