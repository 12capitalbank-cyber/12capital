export default function Home() {
  return (
    <div className="flex flex-col min-h-screen bg-[#070D18] text-slate-100 antialiased selection:bg-amber-500/20 selection:text-amber-300">
      {/* ─── COMPLIANCE & OPERATIONAL BANNER ─── */}
      <div className="bg-[#0B1528] border-b border-slate-800 text-xs py-2.5 px-4 text-center text-slate-400">
        <div className="max-w-7xl mx-auto flex flex-wrap items-center justify-center gap-x-6 gap-y-1">
          <span className="inline-flex items-center gap-2">
            <span className="w-2 h-2 rounded-full bg-emerald-400 animate-pulse"></span>
            <strong className="text-slate-200">Operação Ativa:</strong> Corretora internacional com execução 100% STP / Non-Dealing Desk.
          </span>
          <span className="hidden sm:inline text-slate-600">|</span>
          <span>Provedor de Liquidez: <strong className="text-slate-300 font-mono">Luramic</strong></span>
          <span className="hidden sm:inline text-slate-600">|</span>
          <span>Plataforma & CRM: <strong className="text-slate-300 font-mono">Kenmore Design</strong></span>
          <span className="hidden sm:inline text-slate-600">|</span>
          <span className="text-amber-400 font-semibold">12 Group Holding</span>
        </div>
      </div>

      {/* ─── NAVIGATION ─── */}
      <header className="sticky top-0 z-50 backdrop-blur-md bg-[#070D18]/90 border-b border-slate-800/80">
        <div className="max-w-7xl mx-auto px-6 h-20 flex items-center justify-between">
          <div className="flex items-center gap-4">
            <div className="flex flex-col">
              <span className="font-extrabold text-2xl tracking-tight text-white font-mono flex items-center gap-2">
                12<span className="text-amber-400">CAPITAL</span>
              </span>
              <span className="text-[10px] tracking-widest uppercase font-semibold text-slate-400">
                IBC Saint Lucia • Global Wealth & Multi-Asset
              </span>
            </div>
          </div>

          <nav className="hidden lg:flex items-center gap-8 text-sm font-medium text-slate-300">
            <a href="#cambio-global" className="hover:text-amber-400 transition-colors">Câmbio Global</a>
            <a href="#mercados" className="hover:text-amber-400 transition-colors">Mercados & Ativos</a>
            <a href="#estruturacao" className="hover:text-amber-400 transition-colors">Estruturação Patrimonial</a>
            <a href="#terminal" className="hover:text-amber-400 transition-colors">12 Terminal AI</a>
            <a href="#ecossistema" className="hover:text-amber-400 transition-colors">Ecossistema 12 Group</a>
            <a href="#compliance" className="hover:text-amber-400 transition-colors">Compliance & Risco</a>
          </nav>

          <div className="flex items-center gap-3">
            <a
              href="#client-portal"
              className="hidden sm:inline-flex px-4 py-2 text-xs font-semibold rounded-lg border border-slate-700 bg-slate-800/60 hover:bg-slate-700/80 text-slate-200 transition-all"
            >
              Área do Cliente (Cabinet)
            </a>
            <a
              href="#onboarding"
              className="inline-flex px-5 py-2.5 text-xs font-bold rounded-lg bg-gradient-to-r from-amber-500 to-amber-600 hover:from-amber-400 hover:to-amber-500 text-slate-950 transition-all shadow-lg shadow-amber-500/10"
            >
              Onboarding Institucional
            </a>
          </div>
        </div>
      </header>

      <main className="flex-1">
        {/* ─── HERO SECTION ─── */}
        <section className="relative pt-20 pb-20 px-6 overflow-hidden">
          <div className="absolute inset-0 bg-[radial-gradient(ellipse_80%_80%_at_50%_-20%,rgba(120,119,198,0.15),rgba(255,255,255,0))]"></div>
          
          <div className="max-w-5xl mx-auto text-center relative z-10">
            <div className="inline-flex items-center gap-2 px-3.5 py-1.5 rounded-full bg-slate-800/80 border border-slate-700 text-xs font-semibold text-amber-300 mb-8">
              <span>Membro do 12 Group Holding</span>
              <span className="text-slate-500">•</span>
              <span>Estrutura Societária IBC em Saint Lucia</span>
              <span className="text-slate-500">•</span>
              <span className="text-emerald-400 font-mono">Operação Ativa</span>
            </div>

            <h1 className="text-4xl sm:text-6xl font-extrabold tracking-tight text-white leading-tight mb-8">
              Infraestrutura Financeira Global, <br className="hidden sm:block" />
              <span className="text-transparent bg-clip-text bg-gradient-to-r from-amber-200 via-amber-400 to-amber-500">
                Câmbio Internacional & Alta Governança
              </span>
            </h1>

            <p className="max-w-3xl mx-auto text-lg text-slate-300 leading-relaxed mb-10">
              Conectamos grandes empresários, investidores e instituições a mercados internacionais através de execução transparente sem mesa proprietária (STP/NDD), liquidez institucional via Luramic e inteligência financeira avançada.
            </p>

            <div className="flex flex-col sm:flex-row items-center justify-center gap-4 mb-16">
              <a
                href="#cambio-global"
                className="w-full sm:w-auto px-8 py-3.5 rounded-xl font-bold text-sm bg-amber-400 hover:bg-amber-300 text-slate-950 transition-all shadow-xl shadow-amber-400/15"
              >
                Acessar Plataforma & Mercados
              </a>
              <a
                href="#compliance"
                className="w-full sm:w-auto px-8 py-3.5 rounded-xl font-semibold text-sm border border-slate-700 hover:border-slate-500 bg-slate-900/60 text-slate-200 transition-all"
              >
                Políticas de Compliance & Risco
              </a>
            </div>

            {/* TRUST PILLARS */}
            <div className="grid grid-cols-2 md:grid-cols-4 gap-4 max-w-4xl mx-auto pt-8 border-t border-slate-800/80 text-left">
              <div className="p-4 rounded-xl bg-slate-900/40 border border-slate-800">
                <div className="text-amber-400 text-lg font-bold font-mono">100% STP</div>
                <div className="text-xs text-slate-400 font-medium mt-1">Execução Direta ao Mercado (Sem Risco de Mesa)</div>
              </div>
              <div className="p-4 rounded-xl bg-slate-900/40 border border-slate-800">
                <div className="text-amber-400 text-lg font-bold font-mono">Luramic LP</div>
                <div className="text-xs text-slate-400 font-medium mt-1">Liquidez Institucional Tier-1 Agregada</div>
              </div>
              <div className="p-4 rounded-xl bg-slate-900/40 border border-slate-800">
                <div className="text-amber-400 text-lg font-bold font-mono">Kenmore CRM</div>
                <div className="text-xs text-slate-400 font-medium mt-1">Portal do Cliente, KYC & Hub de PSPs</div>
              </div>
              <div className="p-4 rounded-xl bg-slate-900/40 border border-slate-800">
                <div className="text-amber-400 text-lg font-bold font-mono">Segregação</div>
                <div className="text-xs text-slate-400 font-medium mt-1">Fundos de Clientes 100% Segregados</div>
              </div>
            </div>

            {/* CINEMATIC HERO SHOWCASE */}
            <div className="mt-14 max-w-5xl mx-auto relative rounded-3xl overflow-hidden border border-slate-700/80 shadow-[0_20px_50px_rgba(0,0,0,0.8)]">
              <img
                src="/assets/hero_terminal.jpg"
                alt="12 Capital Institutional Trading Floor"
                className="w-full h-[380px] sm:h-[480px] object-cover"
              />
              <div className="absolute inset-0 bg-gradient-to-t from-[#070D18] via-transparent to-transparent"></div>
              <div className="absolute bottom-6 left-6 right-6 p-4 sm:p-6 rounded-2xl bg-slate-900/85 backdrop-blur-md border border-slate-700/80 flex flex-wrap items-center justify-between gap-4">
                <div>
                  <div className="text-sm font-bold text-white flex items-center gap-2">
                    <span className="w-2.5 h-2.5 rounded-full bg-emerald-400 animate-pulse"></span>
                    Mesa Institucional 12 Capital • Conectividade STP em Tempo Real
                  </div>
                  <div className="text-xs text-slate-400 mt-1">
                    Spreads Brutos Interbancários via Luramic • Latência Sub-1ms (London Equinix LD4)
                  </div>
                </div>
                <div className="flex items-center gap-3">
                  <span className="text-xs font-mono font-bold px-3 py-1.5 rounded-lg bg-amber-400/10 text-amber-400 border border-amber-400/20">
                    A-BOOK ONLY
                  </span>
                  <span className="text-xs font-mono font-bold px-3 py-1.5 rounded-lg bg-emerald-400/10 text-emerald-400 border border-emerald-400/20">
                    LIVE TRADING
                  </span>
                </div>
              </div>
            </div>
          </div>
        </section>

        {/* ─── CÂMBIO GLOBAL & MULTI-ATIVOS ─── */}
        <section id="cambio-global" className="py-24 px-6 bg-[#091120] border-y border-slate-800/80">
          <div className="max-w-7xl mx-auto">
            <div className="text-center max-w-3xl mx-auto mb-16">
              <div className="text-xs uppercase font-bold tracking-widest text-amber-400 mb-3">Execução Institucional</div>
              <h2 className="text-3xl sm:text-4xl font-extrabold text-white">Câmbio Global & Ativos Internacionais</h2>
              <p className="text-slate-400 text-base mt-4">
                Superamos o estigma de corretoras de varejo oferecendo um ambiente sóbrio, transparente e conectado aos maiores centros de liquidez do mundo.
              </p>
            </div>

            <div id="mercados" className="grid md:grid-cols-3 gap-6">
              {/* Câmbio Global */}
              <div className="p-6 rounded-2xl bg-[#0E1A2E] border border-slate-800 hover:border-slate-700 transition-all">
                <div className="w-12 h-12 rounded-xl bg-amber-500/10 border border-amber-500/20 flex items-center justify-center text-amber-400 font-bold mb-4 font-mono">
                  FX
                </div>
                <h3 className="text-xl font-bold text-white mb-2">Câmbio Internacional</h3>
                <p className="text-sm text-slate-400 leading-relaxed mb-4">
                  Negociação de mais de 55 pares de moedas globais (Majors, Minors e Exóticas) com spreads interbancários brutos a partir de 0.0 pips em contas ECN.
                </p>
                <div className="text-xs text-amber-400/90 font-mono font-semibold">Execução STP • Roteamento Luramic</div>
              </div>

              {/* Metais Preciosos */}
              <div className="p-6 rounded-2xl bg-[#0E1A2E] border border-slate-800 hover:border-slate-700 transition-all">
                <div className="w-12 h-12 rounded-xl bg-amber-500/10 border border-amber-500/20 flex items-center justify-center text-amber-400 font-bold mb-4 font-mono">
                  AU
                </div>
                <h3 className="text-xl font-bold text-white mb-2">Ouro, Prata & Commodities</h3>
                <p className="text-sm text-slate-400 leading-relaxed mb-4">
                  Proteção de valor em Ouro Spot (XAU/USD), Prata (XAG/USD) e energia (Petróleo WTI, Brent e Gás Natural) com liquidez contínua e sem requotes.
                </p>
                <div className="text-xs text-amber-400/90 font-mono font-semibold">Profundidade de Livro • Hedging Real</div>
              </div>

              {/* Índices & Ações Globais */}
              <div className="p-6 rounded-2xl bg-[#0E1A2E] border border-slate-800 hover:border-slate-700 transition-all">
                <div className="w-12 h-12 rounded-xl bg-amber-500/10 border border-amber-500/20 flex items-center justify-center text-amber-400 font-bold mb-4 font-mono">
                  IDX
                </div>
                <h3 className="text-xl font-bold text-white mb-2">Índices & Ações Globais</h3>
                <p className="text-sm text-slate-400 leading-relaxed mb-4">
                  Acesso aos principais índices mundiais (S&P 500, Dow Jones, Nasdaq 100, DAX 40) e ações americanas com execução automatizada e margens eficientes.
                </p>
                <div className="text-xs text-amber-400/90 font-mono font-semibold">Sub-milissegundo • Espec / Alocação</div>
              </div>
            </div>
          </div>
        </section>

        {/* ─── ESTRUTURAÇÃO PATRIMONIAL ─── */}
        <section id="estruturacao" className="py-24 px-6 bg-[#070D18]">
          <div className="max-w-7xl mx-auto">
            <div className="grid lg:grid-cols-2 gap-16 items-center">
              <div>
                <div className="text-xs uppercase font-bold tracking-widest text-amber-400 mb-3">Proteção & Governança</div>
                <h2 className="text-3xl sm:text-4xl font-extrabold text-white mb-6">
                  Estruturação Patrimonial Internacional com KYC/AML Robusto
                </h2>
                <p className="text-slate-300 text-base leading-relaxed mb-6">
                  Atendemos grandes empresários, famílias empresárias e instituições filantrópicas que buscam diversificação de risco jurisdicional e alocação segura em moeda forte, com total conformidade jurídica e documental.
                </p>
                <ul className="space-y-4 text-sm text-slate-300 mb-8">
                  <li className="flex items-start gap-3">
                    <span className="text-amber-400 font-bold text-base mt-0.5">✓</span>
                    <span><strong>Governança Offshore Sólida:</strong> Apoio em estruturas corporativas internacionais (IBCs) registradas em Saint Lucia e jurisdições cooperantes com a OCDE.</span>
                  </li>
                  <li className="flex items-start gap-3">
                    <span className="text-amber-400 font-bold text-base mt-0.5">✓</span>
                    <span><strong>Segregação Rigorosa de Risco:</strong> Processos formais de Due Diligence, comprovação documental de origem dos recursos (Source of Wealth) e rastreabilidade total.</span>
                  </li>
                  <li className="flex items-start gap-3">
                    <span className="text-amber-400 font-bold text-base mt-0.5">✓</span>
                    <span><strong>Relacionamento Dedicado:</strong> Atendimento próximo e consultivo, com suporte a Introducing Brokers (IBs) e parcerias institucionais qualificadas.</span>
                  </li>
                </ul>
                <a
                  href="#onboarding"
                  className="inline-flex px-6 py-3 rounded-xl font-bold text-sm bg-slate-800 hover:bg-slate-700 text-slate-100 border border-slate-700 transition-all"
                >
                  Consultar Equipe Institucional
                </a>
              </div>

              {/* BOARD & WEALTH IMAGE CARD */}
              <div className="rounded-3xl overflow-hidden border border-slate-800 shadow-2xl relative">
                <img
                  src="/assets/board_wealth.jpg"
                  alt="12 Group Board Governance & Private Wealth"
                  className="w-full h-[400px] object-cover"
                />
                <div className="absolute inset-0 bg-gradient-to-t from-[#070D18] via-transparent to-transparent"></div>
                <div className="absolute bottom-6 left-6 right-6 p-4 rounded-xl bg-slate-900/85 backdrop-blur-md border border-slate-800">
                  <div className="text-xs font-mono font-bold text-amber-400 uppercase tracking-widest mb-1">
                    Governança Corporativa
                  </div>
                  <div className="text-sm font-bold text-white">
                    Cláudio (CEO) • André (Governança) • Fayson Santos (Tecnologia & Operações)
                  </div>
                  <div className="text-xs text-slate-400 mt-1">
                    Estrutura fiduciária sob Common Law • Segregação de riscos entre holding e subsidiárias
                  </div>
                </div>
              </div>
            </div>
          </div>
        </section>


        {/* ─── 12 TERMINAL AI ─── */}
        <section id="terminal" className="py-24 px-6 bg-[#091120] border-t border-slate-800/80">
          <div className="max-w-7xl mx-auto">
            <div className="text-center max-w-3xl mx-auto mb-16">
              <div className="text-xs uppercase font-bold tracking-widest text-amber-400 mb-3">Inteligência Financeira</div>
              <h2 className="text-3xl sm:text-4xl font-extrabold text-white">12 Intelligence Terminal</h2>
              <p className="text-slate-400 text-base mt-4">
                Espaço de trabalho inteligente com auditoria preditiva de balanços (DRE) via Inteligência Artificial e monitor macroeconômico global em tempo real.
              </p>
            </div>

            <div className="rounded-3xl bg-[#0B1528] border border-slate-800 p-8 lg:p-12 shadow-2xl">
              <div className="grid lg:grid-cols-2 gap-10 items-center mb-10">
                <div>
                  <div className="text-xs font-mono font-bold text-amber-400 uppercase tracking-widest mb-3">
                    Terminal Inteligente Multi-Ativos
                  </div>
                  <h3 className="text-2xl font-bold text-white mb-4">
                    Auditoria Preditiva de Balanços & Radar Macroeconômico
                  </h3>
                  <p className="text-slate-300 text-sm leading-relaxed mb-6">
                    Desenvolvido para investidores corporativos e gestores de patrimônio: faça upload do balanço ou DRE da sua empresa e receba diagnóstico instantâneo de liquidez, solvência (Altman Z-Score) e capacidade de alocação internacional.
                  </p>
                  <div className="grid grid-cols-2 gap-4 text-xs font-mono">
                    <div className="p-3 rounded-lg bg-slate-900/60 border border-slate-800">
                      <div className="text-slate-400">Score de Solvência</div>
                      <div className="text-emerald-400 font-bold text-base mt-1">94.2 / 100</div>
                    </div>
                    <div className="p-3 rounded-lg bg-slate-900/60 border border-slate-800">
                      <div className="text-slate-400">Roteamento STP</div>
                      <div className="text-amber-400 font-bold text-base mt-1">Luramic Direct</div>
                    </div>
                  </div>
                </div>

                <div className="rounded-2xl overflow-hidden border border-slate-800 shadow-2xl relative">
                  <img
                    src="/assets/multi_asset_app.jpg"
                    alt="12 Intelligence Terminal and Mobile Trading"
                    className="w-full h-[320px] object-cover"
                  />
                  <div className="absolute inset-0 bg-gradient-to-t from-[#0B1528] via-transparent to-transparent"></div>
                  <div className="absolute bottom-3 left-4 right-4 text-[11px] font-mono text-slate-300 bg-slate-950/80 px-3 py-1.5 rounded-lg backdrop-blur-sm border border-slate-800">
                    Terminal 12 Capital: Análise de Balanços + Cotação Spot XAU/USD
                  </div>
                </div>
              </div>
            </div>
          </div>
        </section>

        {/* ─── ECOSSISTEMA 12 GROUP ─── */}
        <section id="ecossistema" className="py-24 px-6 bg-[#070D18]">
          <div className="max-w-7xl mx-auto">
            <div className="text-center max-w-3xl mx-auto mb-16">
              <div className="text-xs uppercase font-bold tracking-widest text-amber-400 mb-3">Solidez Corporativa</div>
              <h2 className="text-3xl sm:text-4xl font-extrabold text-white">O Ecossistema 12 Group</h2>
              <p className="text-slate-400 text-base mt-4">
                A 12 Capital é o pilar financeiro internacional de uma holding multissetorial com empresas reais em energia sustentável, tecnologia e agronegócio.
              </p>
            </div>

            <div className="grid md:grid-cols-3 gap-6 mb-8">
              <div className="p-8 rounded-3xl bg-[#0E1A2E] border border-slate-800 flex flex-col justify-between">
                <div>
                  <div className="text-xs font-mono font-bold text-amber-400 uppercase tracking-widest mb-3">Infraestrutura Financeira</div>
                  <h3 className="text-xl font-bold text-white mb-2">12 Capital Inc.</h3>
                  <p className="text-xs text-slate-300 leading-relaxed mb-4">
                    Motor financeiro internacional sediado em Saint Lucia (IBC). Focado em câmbio global, conexão multi-ativos e estruturação patrimonial para investidores internacionais.
                  </p>
                </div>
                <div className="text-[11px] font-mono text-emerald-400">Regulação Internacional • Saint Lucia</div>
              </div>

              <div className="rounded-3xl bg-[#0E1A2E] border border-slate-800 overflow-hidden flex flex-col">
                <img
                  src="/assets/energy_solar.jpg"
                  alt="Detronic Energia Solar Plant"
                  className="w-full h-44 object-cover"
                />
                <div className="p-6 flex flex-col justify-between flex-1">
                  <div>
                    <div className="text-xs font-mono font-bold text-amber-400 uppercase tracking-widest mb-2">Energia Renovável</div>
                    <h3 className="text-lg font-bold text-white mb-2">Detronic Energia</h3>
                    <p className="text-xs text-slate-300 leading-relaxed mb-3">
                      Empresa operacional de geração solar fotovoltaica com receita real e contratos de longo prazo no Brasil, conferindo lastro tangível ao grupo.
                    </p>
                  </div>
                  <div className="text-[11px] font-mono text-emerald-400">Ativos Reais • Energia Solar Fotovoltaica</div>
                </div>
              </div>

              <div className="p-8 rounded-3xl bg-[#0E1A2E] border border-slate-800 flex flex-col justify-between">
                <div>
                  <div className="text-xs font-mono font-bold text-amber-400 uppercase tracking-widest mb-3">Tecnologia & Sistemas</div>
                  <h3 className="text-xl font-bold text-white mb-2">FactorHub / FactorOne</h3>
                  <p className="text-xs text-slate-300 leading-relaxed mb-4">
                    Braço tecnológico do grupo responsável por desenvolvimento de sistemas e pela trilha bancária doméstica no Brasil (via BaaS e futura licença BACEN).
                  </p>
                </div>
                <div className="text-[11px] font-mono text-blue-400">Trilha Regulatória Doméstica Separada</div>
              </div>
            </div>

            {/* SEPARAÇÃO REGULATÓRIA FORMAL */}
            <div className="p-6 rounded-2xl bg-slate-900/60 border border-slate-800 text-xs text-slate-300 leading-relaxed">
              <strong className="text-amber-400">Nota de Governança & Segregação Regulatória:</strong> A 12 Capital Inc. (Saint Lucia) e a FactorOne (Brasil) operam em trilhas societárias e regulatórias estritamente separadas. A 12 Capital não capta ativamente poupança pública nem valores mobiliários no Brasil sem autorização da CVM/BACEN, atuando exclusivamente sob regulação internacional e em regime de contratação transfronteiriça com investidores elegíveis.
            </div>
          </div>
        </section>

        {/* ─── PARCEIROS & COMPLIANCE ─── */}
        <section id="compliance" className="py-24 px-6 bg-[#091120] border-t border-slate-800/80">
          <div className="max-w-7xl mx-auto">
            <div className="text-center max-w-3xl mx-auto mb-16">
              <div className="text-xs uppercase font-bold tracking-widest text-amber-400 mb-3">Conformidade & Risco</div>
              <h2 className="text-3xl sm:text-4xl font-extrabold text-white">Parceiros Estratégicos & Políticas de Segurança</h2>
              <p className="text-slate-400 text-base mt-4">
                Estrutura auditável desenvolvida para atender às exigências de oficiais de compliance bancário e analistas de risco internacional.
              </p>
            </div>

            {/* GLOBAL HIGHWAYS IMAGE BANNER */}
            <div className="mb-14 rounded-3xl overflow-hidden border border-slate-800 shadow-2xl relative">
              <img
                src="/assets/global_network.jpg"
                alt="12 Capital Global Financial Highways"
                className="w-full h-[320px] sm:h-[400px] object-cover"
              />
              <div className="absolute inset-0 bg-gradient-to-t from-[#091120] via-transparent to-transparent"></div>
              <div className="absolute bottom-6 left-6 right-6 p-4 sm:p-6 rounded-2xl bg-slate-950/80 backdrop-blur-md border border-slate-800 flex flex-wrap items-center justify-between gap-4">
                <div>
                  <div className="text-sm font-bold text-white font-mono">
                    ROTEAMENTO STP GLOBAL • SUB-1MS LATENCY
                  </div>
                  <div className="text-xs text-slate-400 mt-1">
                    Conexões diretas de fibra óptica entre Saint Lucia, London Equinix LD4, New York NY4 e Frankfurt.
                  </div>
                </div>
                <span className="text-xs font-mono font-bold px-3 py-1.5 rounded-lg bg-blue-500/10 text-blue-400 border border-blue-500/20">
                  LATÊNCIA 0.89ms (LD4)
                </span>
              </div>
            </div>

            <div className="grid md:grid-cols-2 gap-8 mb-12">
              <div className="p-8 rounded-3xl bg-[#0E1A2E] border border-slate-800">
                <div className="flex items-center justify-between mb-4">
                  <div className="text-2xl font-extrabold text-white font-mono">LURAMIC</div>
                  <span className="px-3 py-1 rounded-full text-xs font-bold bg-amber-400/10 text-amber-400 border border-amber-400/20 font-mono">Prime Liquidity</span>
                </div>
                <h4 className="text-base font-bold text-white mb-2">Provedor Institucional de Liquidez</h4>
                <p className="text-xs text-slate-300 leading-relaxed">
                  Agregação de liquidez de múltiplos bancos de primeira linha, garantindo execução STP direta, spreads brutos e conciliação contábil diária automatizada para monitoramento de risco.
                </p>
              </div>

              <div className="p-8 rounded-3xl bg-[#0E1A2E] border border-slate-800">
                <div className="flex items-center justify-between mb-4">
                  <div className="text-2xl font-extrabold text-white font-mono">KENMORE DESIGN</div>
                  <span className="px-3 py-1 rounded-full text-xs font-bold bg-blue-400/10 text-blue-400 border border-blue-400/20 font-mono">Enterprise Suite</span>
                </div>
                <h4 className="text-base font-bold text-white mb-2">CRM, Trader&apos;s Room & Orquestração de PSPs</h4>
                <p className="text-xs text-slate-300 leading-relaxed">
                  Líder global em software institucional para corretoras, provendo nosso portal do cliente seguro, esteira automatizada de verificação de documentos KYC e gateway de pagamentos regulados.
                </p>
              </div>
            </div>

            <div className="grid sm:grid-cols-3 gap-6">
              <div className="p-6 rounded-2xl bg-[#0E1A2E] border border-slate-800">
                <div className="text-amber-400 font-mono font-bold text-sm mb-2">01. Verificação KYC em 3 Níveis</div>
                <p className="text-xs text-slate-300 leading-relaxed">
                  Validação de documento oficial com biometria facial 3D, comprovante de residência recente e comprovação documental de origem dos recursos (Source of Wealth) para contas institucionais.
                </p>
              </div>

              <div className="p-6 rounded-2xl bg-[#0E1A2E] border border-slate-800">
                <div className="text-amber-400 font-mono font-bold text-sm mb-2">02. Segregação Total de Fundos</div>
                <p className="text-xs text-slate-300 leading-relaxed">
                  Contas de margem dos clientes são estritamente isoladas do caixa corporativo e operacional da 12 Capital. Recursos de clientes nunca são usados para despesas operacionais ou empréstimos internos.
                </p>
              </div>

              <div className="p-6 rounded-2xl bg-[#0E1A2E] border border-slate-800">
                <div className="text-amber-400 font-mono font-bold text-sm mb-2">03. Regra Anti-Terceiros (1st Party)</div>
                <p className="text-xs text-slate-300 leading-relaxed">
                  Depósitos e saques só são aceitos a partir de contas bancárias de mesma titularidade comprovada do cliente cadastrado. Proibição absoluta de pagamentos em espécie ou por terceiros.
                </p>
              </div>
            </div>
          </div>
        </section>

        {/* ─── ONBOARDING CTA ─── */}
        <section id="onboarding" className="py-20 px-6 bg-gradient-to-b from-[#091120] to-[#070D18] text-center">
          <div className="max-w-4xl mx-auto p-12 rounded-3xl bg-[#0E1A2E] border border-slate-800 shadow-2xl">
            <h2 className="text-3xl font-extrabold text-white mb-4">Abertura de Conta & Atendimento Institucional</h2>
            <p className="text-slate-300 text-sm max-w-xl mx-auto mb-8">
              Acesse liquidez institucional de câmbio global e assessoria em estruturação patrimonial com transparência e governança de ponta a ponta.
            </p>
            <div className="flex flex-col sm:flex-row items-center justify-center gap-4">
              <a
                href="#client-portal"
                className="w-full sm:w-auto px-8 py-3.5 rounded-xl font-bold text-sm bg-amber-400 hover:bg-amber-300 text-slate-950 transition-all shadow-xl shadow-amber-400/10"
              >
                Cadastrar Nova Conta
              </a>
              <a
                href="#compliance"
                className="w-full sm:w-auto px-8 py-3.5 rounded-xl font-semibold text-sm border border-slate-700 bg-slate-800/80 text-slate-200 hover:bg-slate-700 transition-all"
              >
                Solicitar Dossiê de Compliance
              </a>
            </div>
          </div>
        </section>
      </main>

      {/* ─── FOOTER ─── */}
      <footer className="bg-[#050912] border-t border-slate-800/80 text-xs text-slate-400 py-16 px-6">
        <div className="max-w-7xl mx-auto grid md:grid-cols-4 gap-10 mb-12">
          <div className="md:col-span-2">
            <span className="font-extrabold text-xl text-white font-mono flex items-center gap-2 mb-3">
              12<span className="text-amber-400">CAPITAL</span>
            </span>
            <p className="text-slate-400 text-xs leading-relaxed max-w-md mb-4">
              12 Capital Inc. é uma International Business Company incorporada sob o International Business Companies Act, Cap. 12.14 das Leis de Saint Lucia. Empresa do 12 Group Holding.
            </p>
            <div className="text-[11px] font-mono text-slate-500">
              Sede Registrada: Saint Lucia • Parceiros Operacionais: Luramic & Kenmore Design
            </div>
          </div>

          <div>
            <div className="font-bold text-slate-200 uppercase tracking-widest text-[11px] mb-4">Produtos & Soluções</div>
            <ul className="space-y-2 text-xs">
              <li><a href="#cambio-global" className="hover:text-slate-200">Câmbio Internacional</a></li>
              <li><a href="#mercados" className="hover:text-slate-200">Ouro, Prata & Petróleo</a></li>
              <li><a href="#mercados" className="hover:text-slate-200">Índices Globais</a></li>
              <li><a href="#estruturacao" className="hover:text-slate-200">Estruturação Patrimonial</a></li>
              <li><a href="#terminal" className="hover:text-slate-200">12 Intelligence Terminal</a></li>
            </ul>
          </div>

          <div>
            <div className="font-bold text-slate-200 uppercase tracking-widest text-[11px] mb-4">Governança & Segurança</div>
            <ul className="space-y-2 text-xs">
              <li><a href="#compliance" className="hover:text-slate-200">Política de AML / CFT</a></li>
              <li><a href="#compliance" className="hover:text-slate-200">Segregação de Fundos</a></li>
              <li><a href="#compliance" className="hover:text-slate-200">Execução STP (Luramic)</a></li>
              <li><a href="#compliance" className="hover:text-slate-200">Jurisdições Proibidas</a></li>
            </ul>
          </div>
        </div>

        {/* STATUTORY REGULATORY DISCLAIMER */}
        <div className="max-w-7xl mx-auto pt-8 border-t border-slate-800/60 space-y-3 text-[11px] text-slate-400 leading-relaxed">
          <p>
            <strong>Avisos Regulatórios & Jurisdicionais:</strong> A 12 Capital Inc. é constituída sob a legislação de Saint Lucia (International Business Companies Act, Cap. 12.14). A 12 Capital Inc. não capta recursos publicamente nem oferta ativamente produtos e serviços a residentes dos Estados Unidos da América (US Persons), residentes domésticos de Saint Lucia ou jurisdições listadas na Lista Negra/Cinza do GAFI/FATF e sob sanções internacionais (OFAC, ONU, União Europeia).
          </p>
          <p>
            <strong>Aviso de Risco:</strong> A negociação de contratos cambiais e derivativos financeiros alavancados envolve risco expressivo de capital. Os clientes contam com Proteção contra Saldo Negativo (Negative Balance Protection) conforme os termos contratuais de prestação de serviços.
          </p>
          <p className="text-slate-400 text-center pt-4">
            © 2026 12 Capital Inc. Todos os direitos reservados. Uma empresa 12 Group Holding.
          </p>
        </div>
      </footer>
    </div>
  );
}
