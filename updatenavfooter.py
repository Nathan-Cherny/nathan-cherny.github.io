import os

newHeader = """
<header id="site-header" class="header-footer-group">
      <div class="header-inner section-inner">
        <div class="header-titles-wrapper">
          <div class="header-titles">
            <div class="site-logo faux-heading">
              <div class="logo-group">
                <a
                  href="/"
                  class="custom-logo-link"
                  rel="home"
                  aria-current="page"
                  ><img
                    width="1880"
                    height="1411"
                    style="height: 1411px"
                    src="/wp-content/uploads/2020/08/cropped-xSoTec-Logo-w-Name.png"
                    class="custom-logo"
                    alt="xSoTec"
                    decoding="async"
                    fetchpriority="high"
                    srcset="
                      /wp-content/uploads/2020/08/cropped-xSoTec-Logo-w-Name.png           3761w,
                      /wp-content/uploads/2020/08/cropped-xSoTec-Logo-w-Name-300x225.png    300w,
                      /wp-content/uploads/2020/08/cropped-xSoTec-Logo-w-Name-1024x768.png  1024w,
                      /wp-content/uploads/2020/08/cropped-xSoTec-Logo-w-Name-768x576.png    768w,
                      /wp-content/uploads/2020/08/cropped-xSoTec-Logo-w-Name-1536x1153.png 1536w,
                      /wp-content/uploads/2020/08/cropped-xSoTec-Logo-w-Name-2048x1537.png 2048w,
                      /wp-content/uploads/2020/08/cropped-xSoTec-Logo-w-Name-1200x900.png  1200w,
                      /wp-content/uploads/2020/08/cropped-xSoTec-Logo-w-Name-1980x1486.png 1980w
                    "
                    sizes="(max-width: 3761px) 100vw, 3761px" /></a
                ><span class="screen-reader-text">xSoTec</span>
                <div class="header-divider"></div>
                <img
                  src="/media/Partner-Google-for-Education-4-300x104.png"
                  alt="Google for Education Partner"
                  class="nav-partner-img"
                />
              </div>
            </div>
          </div>
          <!-- .header-titles -->

          <button
            class="toggle nav-toggle mobile-nav-toggle"
            data-toggle-target=".menu-modal"
            data-toggle-body-class="showing-menu-modal"
            aria-expanded="false"
            data-set-focus=".close-nav-toggle"
          >
            <span class="toggle-inner">
              <span class="toggle-icon">
                <svg
                  class="svg-icon"
                  aria-hidden="true"
                  role="img"
                  focusable="false"
                  xmlns="http://www.w3.org/2000/svg"
                  width="26"
                  height="7"
                  viewbox="0 0 26 7"
                >
                  <path
                    fill-rule="evenodd"
                    d="M332.5,45 C330.567003,45 329,43.4329966 329,41.5 C329,39.5670034 330.567003,38 332.5,38 C334.432997,38 336,39.5670034 336,41.5 C336,43.4329966 334.432997,45 332.5,45 Z M342,45 C340.067003,45 338.5,43.4329966 338.5,41.5 C338.5,39.5670034 340.067003,38 342,38 C343.932997,38 345.5,39.5670034 345.5,41.5 C345.5,43.4329966 343.932997,45 342,45 Z M351.5,45 C349.567003,45 348,43.4329966 348,41.5 C348,39.5670034 349.567003,38 351.5,38 C353.432997,38 355,39.5670034 355,41.5 C355,43.4329966 353.432997,45 351.5,45 Z"
                    transform="translate(-329 -38)"
                  ></path>
                </svg>
              </span>
              <span class="toggle-text">Menu</span>
            </span></button
          ><!-- .nav-toggle -->
        </div>
        <!-- .header-titles-wrapper -->

        <div class="header-navigation-wrapper">
          <nav class="primary-menu-wrapper" aria-label="Horizontal">
            <ul class="primary-menu reset-list-style">
              <li
                id="menu-item-23"
                class="menu-item menu-item-type-custom menu-item-object-custom menu-item-home menu-item-23"
              >
                <a href="/">Home</a>
              </li>
              <li
                id="menu-item-813"
                class="menu-item menu-item-type-post_type menu-item-object-page menu-item-has-children menu-item-813"
              >
                <a>Services</a><span class="icon"></span>
                <ul class="sub-menu">
                  <li
                  id="menu-item-998"
                  class="menu-item menu-item-type-post_type menu-item-object-page menu-item-998"
                  >
                    <a href="/custom-development/">Custom Development</a>
                  </li>
                  <li
                    id="menu-item-964"
                    class="menu-item menu-item-type-post_type menu-item-object-page menu-item-964"
                    >
                    <a href="/advanced-spreadsheet-solutions/"
                      >Advanced Spreadsheet Solutions</a
                    >
                  </li>
                  <li
                    id=""
                    class="menu-item menu-item-type-post_type menu-item-object-page"
                  >
                    <a href="/our-tools/">Build With Our Tools</a>
                  </li>
                  <li
                    id=""
                    class="menu-item menu-item-type-post_type menu-item-object-page"
                  >
                    <a href="/consolidate-data/">Unify Your System's Data</a>
                  </li>
                  <!-- <li
                    id="menu-item-1596"
                    class="menu-item menu-item-type-post_type menu-item-object-page menu-item-1596"
                  >
                    <a href="/sms-signup/">Sign Up for SMS Functionality</a>
                  </li> -->
                </ul>
              </li>
              <li
                id="menu-item-814"
                class="menu-item menu-item-type-post_type menu-item-object-page menu-item-814"
              >
                <a href="/request-a-demo/">Interest Form</a>
              </li>
              <li
                id="menu-item-788"
                class="menu-item menu-item-type-custom menu-item-object-custom menu-item-has-children menu-item-788"
              >
                <a>Meet xSoTec</a><span class="icon"></span>
                <ul class="sub-menu">
                  <li
                    id="menu-item-177"
                    class="menu-item menu-item-type-post_type menu-item-object-page menu-item-177"
                  >
                    <a href="/about-2/">Our Story</a>
                  </li>
                  <li
                    id="menu-item-65"
                    class="menu-item menu-item-type-post_type menu-item-object-page menu-item-65"
                  >
                    <a href="/contact/">Contact Us</a>
                  </li>
                  <li
                    id="menu-item-1026"
                    class="menu-item menu-item-type-post_type menu-item-object-page menu-item-1026"
                  >
                    <a href="/xsotec-blog/">Blog</a>
                  </li>
                </ul>
              </li>
            </ul>
          </nav>
          <!-- .primary-menu-wrapper -->
        </div>
        <!-- .header-navigation-wrapper -->
      </div>
      <!-- .header-inner -->
    </header>
    <!-- #site-header -->

    <div
      class="menu-modal cover-modal header-footer-group"
      data-modal-target-string=".menu-modal"
    >
      <div class="menu-modal-inner modal-inner">
        <div class="menu-wrapper section-inner">
          <div class="menu-top">
            <button
              class="toggle close-nav-toggle fill-children-current-color"
              data-toggle-target=".menu-modal"
              data-toggle-body-class="showing-menu-modal"
              data-set-focus=".menu-modal"
            >
              <span class="toggle-text">Close Menu</span>
              <svg
                class="svg-icon"
                aria-hidden="true"
                role="img"
                focusable="false"
                xmlns="http://www.w3.org/2000/svg"
                width="16"
                height="16"
                viewbox="0 0 16 16"
              >
                <polygon
                  fill=""
                  fill-rule="evenodd"
                  points="6.852 7.649 .399 1.195 1.445 .149 7.899 6.602 14.352 .149 15.399 1.195 8.945 7.649 15.399 14.102 14.352 15.149 7.899 8.695 1.445 15.149 .399 14.102"
                ></polygon>
              </svg></button
            ><!-- .nav-toggle -->

            <nav class="mobile-menu" aria-label="Mobile">
              <ul class="modal-menu reset-list-style">
                <li
                  class="menu-item menu-item-type-custom menu-item-object-custom menu-item-home menu-item-23"
                >
                  <div class="ancestor-wrapper"><a href="/">Home</a></div>
                  <!-- .ancestor-wrapper -->
                </li>
                <li
                  class="menu-item menu-item-type-post_type menu-item-object-page menu-item-has-children menu-item-813"
                >
                  <div class="ancestor-wrapper">
                    <a>Services</a>
                    <button
                      class="toggle sub-menu-toggle fill-children-current-color"
                      data-toggle-target=".menu-modal .menu-item-813 &gt; .sub-menu"
                      data-toggle-type="slidetoggle"
                      data-toggle-duration="250"
                      aria-expanded="false"
                    >
                      <span class="screen-reader-text">Show sub menu</span
                      ><svg
                        class="svg-icon"
                        aria-hidden="true"
                        role="img"
                        focusable="false"
                        xmlns="http://www.w3.org/2000/svg"
                        width="20"
                        height="12"
                        viewbox="0 0 20 12"
                      >
                        <polygon
                          fill=""
                          fill-rule="evenodd"
                          points="1319.899 365.778 1327.678 358 1329.799 360.121 1319.899 370.021 1310 360.121 1312.121 358"
                          transform="translate(-1310 -358)"
                        ></polygon>
                      </svg>
                    </button>
                  </div>
                  <!-- .ancestor-wrapper -->
                  <ul class="sub-menu">
                    <li
                      class="menu-item menu-item-type-post_type menu-item-object-page menu-item-998"
                    >
                      <div class="ancestor-wrapper">
                        <a href="/custom-development/">Custom Development</a>
                      </div>
                      <!-- .ancestor-wrapper -->
                    </li>
                    <li
                      class="menu-item menu-item-type-post_type menu-item-object-page menu-item-964"
                    >
                      <div class="ancestor-wrapper">
                        <a href="/advanced-spreadsheet-solutions/"
                          >Advanced Spreadsheet Solutions</a
                        >
                      </div>
                      <!-- .ancestor-wrapper -->
                    </li>
                    <li
                      class="menu-item menu-item-type-post_type menu-item-object-page menu-item-964"
                    >
                      <div class="ancestor-wrapper">
                        <a href="/our-tools/"
                          >Build With Our Tools</a
                        >
                      </div>
                      <!-- .ancestor-wrapper -->
                    </li>
                    <li
                      class="menu-item menu-item-type-post_type menu-item-object-page menu-item-964"
                    >
                      <div class="ancestor-wrapper">
                        <a href="/consolidate-data/"
                          >Unify Your System's Data</a
                        >
                      </div>
                      <!-- .ancestor-wrapper -->
                    </li>
                  </ul>
                </li>
                <li
                  class="menu-item menu-item-type-post_type menu-item-object-page menu-item-814"
                >
                  <div class="ancestor-wrapper">
                    <a href="/request-a-demo/">Interest Form</a>
                  </div>
                  <!-- .ancestor-wrapper -->
                </li>
                <li
                  class="menu-item menu-item-type-custom menu-item-object-custom menu-item-has-children menu-item-788"
                >
                  <div class="ancestor-wrapper">
                    <a href="#">Meet xSoTec</a
                    ><button
                      class="toggle sub-menu-toggle fill-children-current-color"
                      data-toggle-target=".menu-modal .menu-item-788 &gt; .sub-menu"
                      data-toggle-type="slidetoggle"
                      data-toggle-duration="250"
                      aria-expanded="false"
                    >
                      <span class="screen-reader-text">Show sub menu</span
                      ><svg
                        class="svg-icon"
                        aria-hidden="true"
                        role="img"
                        focusable="false"
                        xmlns="http://www.w3.org/2000/svg"
                        width="20"
                        height="12"
                        viewbox="0 0 20 12"
                      >
                        <polygon
                          fill=""
                          fill-rule="evenodd"
                          points="1319.899 365.778 1327.678 358 1329.799 360.121 1319.899 370.021 1310 360.121 1312.121 358"
                          transform="translate(-1310 -358)"
                        ></polygon>
                      </svg>
                    </button>
                  </div>
                  <!-- .ancestor-wrapper -->
                  <ul class="sub-menu">
                    <li
                      class="menu-item menu-item-type-post_type menu-item-object-page menu-item-177"
                    >
                      <div class="ancestor-wrapper">
                        <a href="/about-2/">Our Story</a>
                      </div>
                      <!-- .ancestor-wrapper -->
                    </li>
                    <li
                      class="menu-item menu-item-type-post_type menu-item-object-page menu-item-65"
                    >
                      <div class="ancestor-wrapper">
                        <a href="/contact/">Contact Us</a>
                      </div>
                      <!-- .ancestor-wrapper -->
                    </li>
                    <li
                      class="menu-item menu-item-type-post_type menu-item-object-page menu-item-1026"
                    >
                      <div class="ancestor-wrapper">
                        <a href="/xsotec-blog/">Blog</a>
                      </div>
                      <!-- .ancestor-wrapper -->
                    </li>
                  </ul>
                </li>
              </ul>
            </nav>
          </div>
          <!-- .menu-top -->

          <div class="menu-bottom"></div>
          <!-- .menu-bottom -->
        </div>
        <!-- .menu-wrapper -->
      </div>
      <!-- .menu-modal-inner -->
    </div>
    <!-- .menu-modal -->
"""

newFooter = """<!-- #site-content -->

    <div
      class="footer-nav-widgets-wrapper header-footer-group"
      style="background-color: var(--brand-ink)"
    >
      <div class="footer-inner section-inner">
        <div class="footer-top has-footer-menu">
          <nav aria-label="Footer" class="footer-menu-wrapper">
            <ul class="footer-menu reset-list-style">
              <li id="menu-item-1012" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-home current-menu-item page_item page-item-977 current_page_item menu-item-1012">
                <a href="/">Home</a>
              </li>
              <li id="menu-item-827" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-827">
                <a href="/services/">Services</a>
              </li>
              <li id="menu-item-999" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-999">
                <a href="/custom-development/">Custom Development</a>
              </li>
              <li id="menu-item-975" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-975">
                <a href="/advanced-spreadsheet-solutions/">Advanced Spreadsheet Solutions</a>
              </li>
              <li id="menu-item-828" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-828">
                <a href="/request-a-demo/">Interest Form</a>
              </li>
              <li id="menu-item-1067" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-1067">
                <a href="/privacy-policy/">Privacy Policy</a>
              </li>
              <li id="menu-item-1542" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-1542">
                <a href="/terms-conditions/">Terms &amp; Conditions</a>
              </li>
            </ul>
          </nav>
          <!-- .site-nav -->
        </div>
        <!-- .footer-top -->
      </div>
      <!-- .footer-inner -->

      <footer id="site-footer" class="header-footer-group">
        <div class="section-inner">
          <div class="footer-credits">
            <p class="footer-copyright">© 2026 <a href="/">xSoTec</a></p>
            <!-- .footer-copyright -->
          </div>
          <!-- .footer-credits -->

          <a class="to-the-top" href="#site-header">
            <span class="to-the-top-long">
              To the top <span class="arrow" aria-hidden="true">↑</span> </span><!-- .to-the-top-long -->
            <span class="to-the-top-short">
              Up <span class="arrow" aria-hidden="true">↑</span> </span><!-- .to-the-top-short --> 
          </a><!-- .to-the-top -->
        </div>
        <!-- .section-inner -->
      </footer>
      <!-- #site-footer -->
    </div>
    <!-- .footer-nav-widgets-wrapper -->"""

directory = "."
extension = ".html"
file_paths = []

# Walk through the directory tree
for root, dirs, files in os.walk(directory):
    for file in files:
        if file.endswith(extension):
            # Join root and file to get the full path
            file_paths.append(os.path.join(root, file))


for fileName in file_paths:
    
    path = fileName.split("\\")[-2]

    with open(fileName, "r", encoding="utf-8") as file:
        htmlContent = file.read()

        # print(path)
        # print([i for i in htmlContent.split("\n") if f"<a href=\"/{path}/\"" in i])

        headerFirstLine = """<header id="site-header" class="header-footer-group">"""
        header = headerFirstLine + htmlContent.split("<!-- #site-header -->")[0].split(headerFirstLine)[1]

        htmlContent = htmlContent.replace(header, newHeader)

        footerFirstLine = "<!-- #site-content -->"
        footerLastLine = "<!-- #site-footer -->"
        
        footer = footerFirstLine + htmlContent.split(footerFirstLine)[1].split(footerLastLine)[0] + footerLastLine
        
        htmlContent = htmlContent.replace(footer, newFooter)

    with open(fileName, "w", encoding="utf-8") as file:
        file.write(htmlContent)