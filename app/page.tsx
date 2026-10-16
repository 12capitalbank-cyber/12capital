const pillars = [
  {
    title: "Trading",
    text: "FX and CFD trading accounts for qualified international clients, on MetaTrader 5.",
  },
  {
    title: "Managed Capital",
    text: "Professionally managed strategies with transparent fee mechanics.",
  },
  {
    title: "Partners",
    text: "Introducing broker and affiliate programmes for professional partners.",
  },
];

export default function Home() {
  return (
    <div className="flex min-h-screen flex-col">
      <div className="bg-[#ece9e1] px-4 py-2 text-center text-[11px] leading-snug text-muted">
        Services of 12 Capital are not directed to residents of the United
        States, Brazil, the United Kingdom, the EU/EEA, Australia, Japan,
        Mainland China, Singapore, India or any jurisdiction where FX/CFD
        distribution is restricted.
      </div>

      <div
        role="status"
        className="bg-green px-4 py-2.5 text-center text-xs uppercase tracking-[0.2em] text-cream"
      >
        Website under construction
      </div>

      <header className="border-b border-black/10 bg-cream">
        <div className="mx-auto flex max-w-6xl items-center px-6 py-5">
          {/* eslint-disable-next-line @next/next/no-img-element */}
          <img src="/logo-12capital.png" alt="12 Capital" className="h-10 w-auto" />
        </div>
      </header>

      <main className="flex-1">
        <section className="relative overflow-hidden bg-mist">
          <div className="mx-auto grid max-w-6xl items-center gap-10 px-6 py-16 md:grid-cols-2 md:py-24">
            <div className="relative z-10">
              <p className="mb-5 text-xs uppercase tracking-[0.25em] text-muted">
                Global markets. Private access.
              </p>
              <h1 className="font-serif text-5xl font-light leading-[1.05] text-green md:text-7xl">
                Something new
                <br />
                is coming.
              </h1>
              <p className="mt-8 max-w-md text-lg leading-relaxed text-muted">
                12 Capital is building a global trading and managed-capital
                platform for qualified international clients. Our website is
                under construction.
              </p>
              <a
                href="mailto:fayson@12capitalbroker.com"
                className="mt-10 inline-block bg-green px-7 py-3.5 text-sm text-cream transition-opacity hover:opacity-90"
              >
                Contact us →
              </a>
            </div>
          </div>
          {/* eslint-disable-next-line @next/next/no-img-element */}
          <img
            src="/hero-lake.jpg"
            alt=""
            className="pointer-events-none absolute inset-y-0 right-0 hidden h-full w-[58%] object-cover md:block"
            style={{
              WebkitMaskImage:
                "linear-gradient(to right, transparent 0%, black 35%)",
              maskImage: "linear-gradient(to right, transparent 0%, black 35%)",
            }}
          />
        </section>

        <section className="mx-auto max-w-6xl px-6 py-20">
          <h2 className="font-serif text-3xl font-light text-green md:text-4xl">
            What we are building
          </h2>
          <div className="mt-10 grid gap-px bg-black/10 md:grid-cols-3">
            {pillars.map((p) => (
              <div key={p.title} className="bg-cream p-8">
                <h3 className="font-serif text-2xl text-green">{p.title}</h3>
                <p className="mt-3 leading-relaxed text-muted">{p.text}</p>
                <p className="mt-6 text-xs uppercase tracking-[0.2em] text-gold">
                  Coming soon
                </p>
              </div>
            ))}
          </div>
        </section>
      </main>

      <footer className="bg-green px-6 py-10 text-xs leading-relaxed text-cream/75">
        <div className="mx-auto max-w-6xl space-y-3">
          <p>
            <strong className="text-cream">Risk warning:</strong> CFDs and FX
            carry a high risk of rapid loss due to leverage. Past performance is
            not a reliable indicator of future results. This page does not
            constitute an offer or solicitation of any service.
          </p>
          <p>
            12 Capital Limited · Saint Lucia IBC · Reg. No. 2026-00606 ·
            Registered office: to be confirmed · fayson@12capitalbroker.com
          </p>
        </div>
      </footer>
    </div>
  );
}
