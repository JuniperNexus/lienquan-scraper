import { Geist as FontSans, Geist_Mono as FontMono } from "next/font/google"

export const sans = FontSans({
  subsets: ["latin"],
  display: "swap",
  variable: "--font-sans",
})

export const mono = FontMono({
  subsets: ["latin"],
  display: "swap",
  variable: "--font-mono",
})
