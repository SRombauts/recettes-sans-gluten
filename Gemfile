source "https://rubygems.org"

# GitHub Pages : reproduit localement l'environnement de build des Pages.
# La dépendance épingle automatiquement Jekyll et les plugins compatibles.
gem "github-pages", group: :jekyll_plugins

# Thème de la documentation (chargé via remote_theme dans _config.yml,
# inclus aussi en gem pour servir le site en local).
gem "just-the-docs"

group :jekyll_plugins do
  gem "jekyll-remote-theme"
  gem "jekyll-relative-links"
  gem "jekyll-seo-tag"
  gem "jekyll-sitemap"
end

# Windows et JRuby ne lisent pas les fuseaux horaires depuis le système.
gem "tzinfo", ">= 1", "< 3"
gem "tzinfo-data", platforms: [:mingw, :x64_mingw, :mswin, :jruby]

# Performance file watcher pour Windows.
gem "wdm", "~> 0.1.1", platforms: [:mingw, :x64_mingw, :mswin]
