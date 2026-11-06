# Instantiatio website

The bilingual research and engineering website for Instantiatio / iEWR.

- [English](https://instantiatio.github.io/ewr/eng/)
- [Русский](https://instantiatio.github.io/ewr/ru/)
- [iEWR agent-native application, documentation and releases](https://github.com/instantiatio/iEWR)

Website source is in `website/`. It uses MkDocs Material, locally served Manrope,
English/Russian content, native search and the existing Plausible analytics snippet.
See [build and maintenance instructions](website/README.md).
GitHub Actions builds, checks and publishes the same artifact to GitHub Pages.

`legacy/` builds the compatibility pages for the former `/iEWR/` website address.
The old application's repository retains only a redirect workflow referencing a
pinned commit here. Its application files, documentation and releases are separate
from this website and are not changed by a website deployment.

Website content and source were migrated from `instantiatio/iEWR` commit
`66b19e954803644708457c2737e682dba0e185ea`. Existing copyright and license notices,
including the original MIT license, are retained verbatim. Website authorship:
**Instantiatio EWR Contributors**. Conceptual and third-party source credits remain
on the website's About pages and in the supplied asset notices.
