function Header() {
  return (
    <header className="site-header">
      <div className="header-inner">
        <div className="brand">
          <div className="brand-mark">CV</div>
          <div className="brand-copy">
            <strong>CareerMatch AI</strong>
            <span>Akıllı CV Eşleştirme</span>
          </div>
        </div>

        <nav className="site-nav">
          <a className="nav-link" href="#anasayfa">
            Ana Sayfa
          </a>
          <a className="nav-link" href="#ozellikler">
            Özellikler
          </a>
          <a className="nav-link" href="#eslestirme">
            Eşleştirme
          </a>
        </nav>
      </div>
    </header>
  );
}

export default Header;

