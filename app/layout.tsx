import type { Metadata } from "next";
import { Geist, Geist_Mono } from "next/font/google";
import "./globals.css";

const geistSans = Geist({
  variable: "--font-geist-sans",
  subsets: ["latin"],
});

const geistMono = Geist_Mono({
  variable: "--font-geist-mono",
  subsets: ["latin"],
});

export const metadata: Metadata = {
  title: "12 Capital — Global Multi-Asset Prime & Wealth Infrastructure",
  description:
    "Institutional multi-asset brokerage, Straight-Through Processing (STP), and financial intelligence for global traders, family offices, and wealth clients. Domiciled in Saint Lucia (IBC).",
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html
      lang="en"
      className={`${geistSans.variable} ${geistMono.variable} h-full antialiased`}
    >
      <body className="min-h-full flex flex-col bg-[#070D18] text-slate-100 font-sans selection:bg-amber-500/20 selection:text-amber-300">
        {children}
      </body>
    </html>
  );
}
