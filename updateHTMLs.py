import os
import json
from datetime import datetime, timezone
from bs4 import BeautifulSoup

DIRECTORY = "."
EXTENSION = ".html"

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
                    src="/wp-content/uploads/2020/08/cropped-xSoTec-Logo-w-Name-2-1024x767.png"
                    class="custom-logo"
                    alt="xSoTec"
                    decoding="async"
                    fetchpriority="high"
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
                    <a href="/transform-your-sheets/"
                      >Organize & Automate Your Sheets</a
                    >
                  </li>
                  <li
                    id=""
                    class="menu-item menu-item-type-post_type menu-item-object-page"
                  >
                    <a href="/consolidate-data/">Unify Your Disparate Data</a>
                  </li>
                  <li
                    id=""
                    class="menu-item menu-item-type-post_type menu-item-object-page"
                  >
                    <a href="/prototype-functional-models/">Prototype Functional Models</a>
                  </li>
                  <li
                    id=""
                    class="menu-item menu-item-type-post_type menu-item-object-page"
                  >
                    <a href="/our-tools/">Use Our Tools</a>
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
                id="menu-item-999"
                class="menu-item menu-item-type-post_type menu-item-object-page menu-item-814"
              >
                <a href="/case-studies/">Success Stories</a>
              </li>
              <li
                id="menu-item-999"
                class="menu-item menu-item-type-post_type menu-item-object-page menu-item-814"
              >
                <a href="/how-we-work/">How We Work</a>
              </li>
              <!-- <li
                id="menu-item-999"
                class="menu-item menu-item-type-post_type menu-item-object-page menu-item-814"
              >
                <a href="/case-studies/">Case Studies</a>
              </li> -->
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
                    <a href="/about/">Our Story</a>
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
                        <a href="/transform-your-sheets/"
                          >Organize & Automate Your Sheets</a
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
                    <li
                      class="menu-item menu-item-type-post_type menu-item-object-page menu-item-964"
                    >
                      <div class="ancestor-wrapper">
                        <a href="/prototype-functional-models/"
                          >Prototype Functional Models</a
                        >
                      </div>
                      <!-- .ancestor-wrapper -->
                    </li>
                    <li
                      class="menu-item menu-item-type-post_type menu-item-object-page menu-item-964"
                    >
                      <div class="ancestor-wrapper">
                        <a href="/our-tools/"
                          >Use Our Tools</a
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
                  id="menu-item-999"
                  class="menu-item menu-item-type-post_type menu-item-object-page menu-item-814"
                >
                  <a href="/case-studies/">Success Stories</a>
                </li>
                <li
                  class="menu-item menu-item-type-post_type menu-item-object-page menu-item-814"
                >
                  <div class="ancestor-wrapper">
                    <a href="/how-we-work/">How We Work</a>
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
                        <a href="/about/">Our Story</a>
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
      <!--#site-header-end-->

      
"""

newFooter = """
    </main>
    <!-- #site-header -->
    <div
      class="footer-nav-widgets-wrapper header-footer-group"
      style="background-color: var(--brand-ink)"
    >
      <div class="footer-inner section-inner">
        <div class="footer-top has-footer-menu">
          <nav aria-label="Footer" class="footer-menu-wrapper">
            <ul class="footer-menu reset-list-style">
              <li
                id="menu-item-1012"
                class="menu-item menu-item-type-post_type menu-item-object-page menu-item-home page_item page-item-977 current_page_item menu-item-1012"
              >
                <a href="/">Home</a>
              </li>
              <li
                id="menu-item-999"
                class="menu-item menu-item-type-post_type menu-item-object-page menu-item-999"
              >
                <a href="/custom-development/">Custom Development</a>
              </li>
              <li
                id="menu-item-975"
                class="menu-item menu-item-type-post_type menu-item-object-page menu-item-975"
              >
                <a href="/transform-your-sheets/"
                  >Organize & Automate Your Sheets</a
                >
              </li>
              <li
                id="menu-item-975"
                class="menu-item menu-item-type-post_type menu-item-object-page menu-item-975"
              >
                <a href="/how-we-work/">How We Work</a>
              </li>
              <li
                id="menu-item-975"
                class="menu-item menu-item-type-post_type menu-item-object-page menu-item-975"
              >
                <a href="/about/">Our Story</a>
              </li>
              <li
                id="menu-item-828"
                class="menu-item menu-item-type-post_type menu-item-object-page menu-item-828"
              >
                <a href="/request-a-demo/">Interest Form</a>
              </li>
              <li
                id="menu-item-1067"
                class="menu-item menu-item-type-post_type menu-item-object-page menu-item-1067"
              >
                <a href="/privacy-policy/">Privacy Policy</a>
              </li>
              <li
                id="menu-item-1542"
                class="menu-item menu-item-type-post_type menu-item-object-page menu-item-1542"
              >
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
            <div class="footer-links">
              <a href="https://www.linkedin.com/company/xsotec" target="_blank"><i class="fa-brands fa-linkedin"></i></a>
              <a href="https://www.facebook.com/xsotec/" target="_blank"><i class="fa-brands fa-square-facebook"></i></a>
            </div>
            <!-- .footer-copyright -->
          </div>
          <!-- .footer-credits -->

          <a class="to-the-top" href="#site-header">
            <span class="to-the-top-long">
              To the top <span class="arrow" aria-hidden="true">↑</span> </span
            ><!-- .to-the-top-long -->
            <span class="to-the-top-short">
              Up <span class="arrow" aria-hidden="true">↑</span> </span
            ><!-- .to-the-top-short --> </a
          ><!-- .to-the-top -->
        </div>
        <!-- .section-inner -->
      </footer>
      <!-- #site-footer -->
    </div>
    <!-- .footer-nav-widgets-wrapper -->"""

newHead = """
<head>
    <meta charset="UTF-8" />

    <meta name="viewport" content="width=device-width, initial-scale=1.0" />

    <link rel="profile" href="https://gmpg.org/xfn/11" />

    <meta
      name="robots"
      content="index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1"
    />
    <!-- Google tag (gtag.js) consent mode dataLayer added by Site Kit -->
    <script id="google_gtagjs-js-consent-mode-data-layer">
      window.dataLayer = window.dataLayer || [];
      function gtag() {
        dataLayer.push(arguments);
      }
      gtag("consent", "default", {
        ad_personalization: "denied",
        ad_storage: "denied",
        ad_user_data: "denied",
        analytics_storage: "denied",
        functionality_storage: "denied",
        security_storage: "denied",
        personalization_storage: "denied",
        region: [
          "AT",
          "BE",
          "BG",
          "CH",
          "CY",
          "CZ",
          "DE",
          "DK",
          "EE",
          "ES",
          "FI",
          "FR",
          "GB",
          "GR",
          "HR",
          "HU",
          "IE",
          "IS",
          "IT",
          "LI",
          "LT",
          "LU",
          "LV",
          "MT",
          "NL",
          "NO",
          "PL",
          "PT",
          "RO",
          "SE",
          "SI",
          "SK",
        ],
        wait_for_update: 500,
      });
      window._googlesitekitConsentCategoryMap = {
        statistics: ["analytics_storage"],
        marketing: ["ad_storage", "ad_user_data", "ad_personalization"],
        functional: ["functionality_storage", "security_storage"],
        preferences: ["personalization_storage"],
      };
      window._googlesitekitConsents = {
        ad_personalization: "denied",
        ad_storage: "denied",
        ad_user_data: "denied",
        analytics_storage: "denied",
        functionality_storage: "denied",
        security_storage: "denied",
        personalization_storage: "denied",
        region: [
          "AT",
          "BE",
          "BG",
          "CH",
          "CY",
          "CZ",
          "DE",
          "DK",
          "EE",
          "ES",
          "FI",
          "FR",
          "GB",
          "GR",
          "HR",
          "HU",
          "IE",
          "IS",
          "IT",
          "LI",
          "LT",
          "LU",
          "LV",
          "MT",
          "NL",
          "NO",
          "PL",
          "PT",
          "RO",
          "SE",
          "SI",
          "SK",
        ],
        wait_for_update: 500,
      };
    </script>
    <!-- End Google tag (gtag.js) consent mode dataLayer added by Site Kit -->

    <!-- This site is optimized with the Yoast SEO plugin v21.9.1 - https://yoast.com/wordpress/plugins/seo/ -->
    <title>xSoTec - District wide solutions built on Google Sheets</title>
    <meta
      name="description"
      content="Build competency-based, restorative behavior, learner profile systems, and more. xSoTec helps you create district-wide solutions specifically for your organization."
    />
    <link rel="canonical" href="/" />
    <meta property="og:locale" content="en_US" />
    <meta property="og:type" content="website" />
    <meta
      property="og:title"
      content="xSoTec - District wide solutions built on Google Sheets"
    />
    <meta
      property="og:description"
      content="Build competency-based, restorative behavior, learner profile systems, and more. xSoTec helps you create district-wide solutions specifically for your organization."
    />
    <meta property="og:url" content="/" />
    <meta property="og:site_name" content="xSoTec" />
    <meta
      property="article:modified_time"
      content="2025-03-19T16:05:17+00:00"
    />
    <meta
      property="og:image"
      content="/wp-content/uploads/2024/01/GfE-Partner-Badges-Horizontal.png"
    />
    <meta name="twitter:card" content="summary_large_image" />
    <script type="application/ld+json" class="yoast-schema-graph">
      {
        "@context": "https://schema.org",
        "@graph": [
          {
            "@type": "WebPage",
            "@id": "/",
            "url": "/",
            "name": "xSoTec - District wide solutions built on Google Sheets",
            "isPartOf": { "@id": "/#website" },
            "about": { "@id": "/#organization" },
            "primaryImageOfPage": { "@id": "/#primaryimage" },
            "image": { "@id": "/#primaryimage" },
            "thumbnailUrl": "/wp-content/uploads/2024/01/GfE-Partner-Badges-Horizontal.png",
            "datePublished": "2023-02-21T16:20:27+00:00",
            "dateModified": "2025-03-19T16:05:17+00:00",
            "description": "Build competency-based, restorative behavior, learner profile systems, and more. xSoTec helps you create district-wide solutions specifically for your organization.",
            "breadcrumb": { "@id": "/#breadcrumb" },
            "inLanguage": "en-US",
            "potentialAction": [{ "@type": "ReadAction", "target": ["/"] }]
          },
          {
            "@type": "ImageObject",
            "inLanguage": "en-US",
            "@id": "/#primaryimage",
            "url": "/wp-content/uploads/2024/01/GfE-Partner-Badges-Horizontal.png",
            "contentUrl": "/wp-content/uploads/2024/01/GfE-Partner-Badges-Horizontal.png",
            "width": 1043,
            "height": 293
          },
          {
            "@type": "BreadcrumbList",
            "@id": "/#breadcrumb",
            "itemListElement": [
              { "@type": "ListItem", "position": 1, "name": "Home" }
            ]
          },
          {
            "@type": "WebSite",
            "@id": "/#website",
            "url": "/",
            "name": "xSoTec",
            "description": "",
            "publisher": { "@id": "/#organization" },
            "potentialAction": [
              {
                "@type": "SearchAction",
                "target": {
                  "@type": "EntryPoint",
                  "urlTemplate": "/?s={search_term_string}"
                },
                "query-input": "required name=search_term_string"
              }
            ],
            "inLanguage": "en-US"
          },
          {
            "@type": "Organization",
            "@id": "/#organization",
            "name": "xSoTec",
            "url": "/",
            "logo": {
              "@type": "ImageObject",
              "inLanguage": "en-US",
              "@id": "/#/schema/logo/image/",
              "url": "/wp-content/uploads/2020/08/cropped-xSoTec-Logo-w-Name.png",
              "contentUrl": "/wp-content/uploads/2020/08/cropped-xSoTec-Logo-w-Name.png",
              "width": 3761,
              "height": 2822,
              "caption": "xSoTec"
            },
            "image": { "@id": "/#/schema/logo/image/" }
          }
        ]
      }
    </script>
    <!-- / Yoast SEO plugin. -->

    <link rel="dns-prefetch" href="//www.googletagmanager.com" />
    <link rel="dns-prefetch" href="//fonts.googleapis.com" />
    <link rel="dns-prefetch" href="//use.fontawesome.com" />
    <link
      rel="alternate"
      type="application/rss+xml"
      title="xSoTec » Feed"
      href="/feed/"
    />
    <link
      rel="alternate"
      type="application/rss+xml"
      title="xSoTec » Comments Feed"
      href="/comments/feed/"
    />
    <link
      rel="alternate"
      title="oEmbed (JSON)"
      type="application/json+oembed"
      href="/wp-json/oembed/1.0/embed?url=%2F"
    />
    <link
      rel="alternate"
      title="oEmbed (XML)"
      type="text/xml+oembed"
      href="/wp-json/oembed/1.0/embed?url=%2F&amp;format=xml"
    />
    <style id="wp-img-auto-sizes-contain-inline-css">
      img:is([sizes="auto" i], [sizes^="auto," i]) {
        contain-intrinsic-size: 3000px 1500px;
      }
      /*# sourceURL=wp-img-auto-sizes-contain-inline-css */
    </style>
    <style id="wp-emoji-styles-inline-css">
      img.wp-smiley,
      img.emoji {
        display: inline !important;
        border: none !important;
        box-shadow: none !important;
        height: 1em !important;
        width: 1em !important;
        margin: 0 0.07em !important;
        vertical-align: -0.1em !important;
        background: none !important;
        padding: 0 !important;
      }
      /*# sourceURL=wp-emoji-styles-inline-css */
    </style>
    <link
      rel="stylesheet"
      id="wp-block-library-css"
      href="/wp-includes/css/dist/block-library/style.min.css?ver=6.9.4"
      media="all"
    />

    <link
      rel="stylesheet"
      id="inline-css"
      href="/wp-content/themes/plugins/inline.css"
      media="all"
    />
    <link
      rel="stylesheet"
      id="coblocks-frontend-css"
      href="/wp-content/plugins/coblocks/dist/style-coblocks-1.css?ver=3.1.5"
      media="all"
    />

    <link
      rel="stylesheet"
      id="coblocks-EXTENSIONs-css"
      href="/wp-content/plugins/coblocks/dist/style-coblocks-EXTENSIONs.css?ver=3.1.5"
      media="all"
    />
    <link
      rel="stylesheet"
      id="coblocks-animation-css"
      href="/wp-content/plugins/coblocks/dist/style-coblocks-animation.css?ver=d9b2b27566e6a2a85d1b"
      media="all"
    />
    <link
      rel="stylesheet"
      id="twentig-blocks-css"
      href="/wp-content/plugins/twentig/dist/blocks/common.css?ver=f41e47526b76d38fc169"
      media="all"
    />
    <link
      rel="stylesheet"
      id="font-awesome-svg-styles-css"
      href="/wp-content/uploads/font-awesome/v6.3.0/css/svg-with-js.css"
      media="all"
    />
    <link
      rel="stylesheet"
      id=""
      href="/wp-content/themes/plugins/fontawesome-global.css"
      media="all"
    />

    <link
      rel="stylesheet"
      id="coblocks-block-fonts-css"
      href="//fonts.googleapis.com/css?family=YrsaMontserratArvoIBM+Plex+Sans%3A100%2C100italic%2C200%2C200italic%2C300%2C300italic%2C400%2C400italic%2C500%2C500italic%2C600%2C600italic%2C700%2C700italic%2C800%2C800italic%2C900%2C900italic%7CAsap%3A100%2C100italic%2C200%2C200italic%2C300%2C300italic%2C400%2C400italic%2C500%2C500italic%2C600%2C600italic%2C700%2C700italic%2C800%2C800italic%2C900%2C900italic%7C&amp;ver=3.1.5"
      media="all"
    />
    <link
      rel="stylesheet"
      id="wp-components-css"
      href="/wp-includes/css/dist/components/style.min.css?ver=6.9.4"
      media="all"
    />
    <link
      rel="stylesheet"
      id="godaddy-styles-css"
      href="/wp-content/mu-plugins/vendor/wpex/godaddy-launch/includes/Dependencies/GoDaddy/Styles/build/latest.css?ver=2.0.2"
      media="all"
    />
    <link
      rel="stylesheet"
      id="twentytwenty-style-css"
      href="/wp-content/themes/twentytwenty/style.css"
      media="all"
    />
    <link
      rel="stylesheet"
      id="twentytwenty-fonts-css"
      href="/wp-content/themes/twentytwenty/assets/css/font-inter.css?ver=3.1"
      media="all"
    />
    <link
      rel="stylesheet"
      id="twentytwenty-print-style-css"
      href="/wp-content/themes/twentytwenty/print.css?ver=3.1"
      media="print"
    />
    <link
      rel="stylesheet"
      id="font-awesome-official-css"
      href="https://use.fontawesome.com/releases/v6.3.0/css/all.css"
      media="all"
      integrity="sha384-nYX0jQk7JxCp1jdj3j2QdJbEJaTvTlhexnpMjwIkYQLdk9ZE3/g8CBw87XP2N0pR"
      crossorigin="anonymous"
    />
    <link
      rel="stylesheet"
      id="twentig-twentytwenty-css"
      href="/wp-content/plugins/twentig/dist/css/twentytwenty/style.css?ver=1.8"
      media="all"
    />
    <style id="twentig-twentytwenty-inline-css">
      ul.primary-menu,
      ul.modal-menu > li .ancestor-wrapper a {
        font-weight: 500;
      }
      body.has-header-opaque .primary-menu > li:not(.menu-button) > a,
      body.has-header-opaque .primary-menu > li > .icon {
        color: #047eb3;
      }
      :root .has-subtle-background-background-color {
        background-color: #f2f2f2;
      }
      :root .has-subtle-background-color.has-text-color {
        color: #f2f2f2;
      }
      /*# sourceURL=twentig-twentytwenty-inline-css */
    </style>
    <link
      rel="stylesheet"
      id="font-awesome-official-v4shim-css"
      href="https://use.fontawesome.com/releases/v6.3.0/css/v4-shims.css"
      media="all"
      integrity="sha384-SQz6YOYE9rzJdPMcxCxNEmEuaYeT0ayZY/ZxArYWtTnvBwcfHI6rCwtgsOonZ+08"
      crossorigin="anonymous"
    />
    <script
      src="/wp-content/themes/twentytwenty/assets/js/index.js?ver=3.1"
      id="twentytwenty-js-js"
      defer
      data-wp-strategy="defer"
    ></script>
    <script
      src="/wp-content/plugins/twentig/dist/js/classic/twentig-twentytwenty.js?ver=1.0"
      id="twentig-twentytwenty-js"
    ></script>

    <!-- Google tag (gtag.js) snippet added by Site Kit -->
    <!-- Google Analytics snippet added by Site Kit -->
    <!-- Google Ads snippet added by Site Kit -->
    <script
      src="https://www.googletagmanager.com/gtag/js?id=GT-MR2R5VG"
      id="google_gtagjs-js"
      async
    ></script>
    <script id="google_gtagjs-js-after">
      window.dataLayer = window.dataLayer || [];
      function gtag() {
        dataLayer.push(arguments);
      }
      gtag("set", "linker", { domains: ["xsotec.com"] });
      gtag("js", new Date());
      gtag("set", "developer_id.dZTNiMT", true);
      gtag("config", "GT-MR2R5VG");
      gtag("config", "AW-11551650356");
      window._googlesitekit = window._googlesitekit || {};
      window._googlesitekit.throttledEvents = [];
      window._googlesitekit.gtagEvent = (name, data) => {
        var key = JSON.stringify({ name, data });
        if (!!window._googlesitekit.throttledEvents[key]) {
          return;
        }
        window._googlesitekit.throttledEvents[key] = true;
        setTimeout(() => {
          delete window._googlesitekit.throttledEvents[key];
        }, 5);
        gtag("event", name, { ...data, event_source: "site-kit" });
      };
      //# sourceURL=google_gtagjs-js-after
    </script>
    <link rel="https://api.w.org/" href="/wp-json/" />
    <link
      rel="alternate"
      title="JSON"
      type="application/json"
      href="/wp-json/wp/v2/pages/977"
    />
    <link
      rel="EditURI"
      type="application/rsd+xml"
      title="RSD"
      href="/xmlrpc.php?rsd"
    />
    <link rel="shortlink" href="/" />
    <meta name="generator" content="Site Kit by Google 1.182.0" />
    <noscript
      ><style>
        .tw-block-animation {
          opacity: 1;
          transform: none;
          clip-path: none;
        }
      </style></noscript
    >
    <script>
      document.documentElement.className =
        document.documentElement.className.replace("no-js", "js");
      //# sourceURL=twentytwenty_no_js_class
    </script>

    <!-- Google AdSense meta tags added by Site Kit -->
    <meta
      name="google-adsense-platform-account"
      content="ca-host-pub-2644536267352236"
    />
    <meta
      name="google-adsense-platform-domain"
      content="sitekit.withgoogle.com"
    />
    <!-- End Google AdSense meta tags added by Site Kit -->
    <style id="custom-background-css">
      body.custom-background {
        background-color: #ffffff;
      }
    </style>

    <!-- Google Tag Manager snippet added by Site Kit -->
    <script>
      (function (w, d, s, l, i) {
        w[l] = w[l] || [];
        w[l].push({ "gtm.start": new Date().getTime(), event: "gtm.js" });
        var f = d.getElementsByTagName(s)[0],
          j = d.createElement(s),
          dl = l != "dataLayer" ? "&l=" + l : "";
        j.async = true;
        j.src = "https://www.googletagmanager.com/gtm.js?id=" + i + dl;
        f.parentNode.insertBefore(j, f);
      })(window, document, "script", "dataLayer", "GTM-KL68LVZ");
    </script>

    <!-- End Google Tag Manager snippet added by Site Kit -->
    <style id="uagb-style-conditional-EXTENSION">
      @media (min-width: 1025px) {
        body .uag-hide-desktop.uagb-google-map__wrap,
        body .uag-hide-desktop {
          display: none !important;
        }
      }
      @media (min-width: 768px) and (max-width: 1024px) {
        body .uag-hide-tab.uagb-google-map__wrap,
        body .uag-hide-tab {
          display: none !important;
        }
      }
      @media (max-width: 767px) {
        body .uag-hide-mob.uagb-google-map__wrap,
        body .uag-hide-mob {
          display: none !important;
        }
      }
    </style>
    <style id="uagb-style-frontend-977">
      .uag-blocks-common-selector {
        z-index: var(--z-index-desktop) !important;
      }
      @media (max-width: 976px) {
        .uag-blocks-common-selector {
          z-index: var(--z-index-tablet) !important;
        }
      }
      @media (max-width: 767px) {
        .uag-blocks-common-selector {
          z-index: var(--z-index-mobile) !important;
        }
      }
    </style>
    <link
      rel="icon"
      href="/wp-content/uploads/2020/08/cropped-xSoTec-Logo-SQUARED-32x32.png"
      sizes="32x32"
    />
    <link
      rel="icon"
      href="/wp-content/uploads/2020/08/cropped-xSoTec-Logo-SQUARED-192x192.png"
      sizes="192x192"
    />
    <link
      rel="apple-touch-icon"
      href="/wp-content/uploads/2020/08/cropped-xSoTec-Logo-SQUARED-180x180.png"
    />
    <meta
      name="msapplication-TileImage"
      content="/wp-content/uploads/2020/08/cropped-xSoTec-Logo-SQUARED-270x270.png"
    />
    <link
      rel="stylesheet"
      id="custom-css"
      href="/wp-content/themes/plugins/custom.css"
      media="all"
    />
    <link
      rel="stylesheet"
      id="main-section"
      href="/wp-includes/css/main-section.css"
      media="all"
    />"""


# ACTUAL CODE

file_paths = []

# Walk through the DIRECTORY tree
for root, dirs, files in os.walk(DIRECTORY):
    for file in files:
        if file.endswith(EXTENSION):
            # Join root and file to get the full path
            file_paths.append(os.path.join(root, file))

for fileName in file_paths:
    # 1. Get the DIRECTORY path of the current file
    dir_path = os.path.dirname(fileName)
    
    # 2. Get the relative path from the base DIRECTORY and normalize slashes for the web
    rel_dir = os.path.relpath(dir_path, DIRECTORY).replace("\\", "/")
    
    # 3. Determine the correct full URL path
    url_path = "/" if rel_dir == "." else f"/{rel_dir}/"

    with open(fileName, "r", encoding="utf-8") as file:
        htmlContent = file.read()

        # -- HEADER --
        # headerFirstLine = """<header id="site-header" class="header-footer-group">"""
        # header = (
        #     headerFirstLine
        #     + htmlContent.split("""<main id="site-content">""")[0].split(headerFirstLine)[1]
        # )
        # htmlContent = htmlContent.replace(header, newHeader)

        # -- CURRENT-MENU-ITEM --
        # (Your menu item logic goes here)

        # -- HEAD --
        headFirstLine = """<head>"""
        if headFirstLine in htmlContent and "</head>" in htmlContent:
            head = headFirstLine + htmlContent.split("</head>")[0].split(headFirstLine)[1]

            # Create a copy of your newHead template for this specific file
            custom_head = newHead
            
            # Update canonical and OG URLs
            custom_head = custom_head.replace(
                '<link rel="canonical" href="/" />', 
                f'<link rel="canonical" href="{url_path}" />'
            )
            custom_head = custom_head.replace(
                '<meta property="og:url" content="/" />', 
                f'<meta property="og:url" content="{url_path}" />'
            )
            
            # Update the Yoast JSON-LD URLs (WebPage ID, URL, and Website ID)
            custom_head = custom_head.replace('"@id": "/"', f'"@id": "{url_path}"')
            custom_head = custom_head.replace('"url": "/"', f'"url": "{url_path}"')
            custom_head = custom_head.replace('"/#website"', f'"{url_path}#website"')
            
            # 4. Generate the dynamic Breadcrumb JSON based on folder depth
            if url_path == "/":
                breadcrumb_json = """{
            "@type": "BreadcrumbList",
            "@id": "/#breadcrumb",
            "itemListElement": [
              { "@type": "ListItem", "position": 1, "name": "Home", "item": "https://xsotec.com/" }
            ]
          }"""
            else:
                # Split the URL path into parts (e.g. ['case-studies', 'b21'])
                parts = [p for p in url_path.split("/") if p]
                
                # Start with the Home item
                items = ['{ "@type": "ListItem", "position": 1, "name": "Home", "item": "https://xsotec.com/" }']
                
                current_path = ""
                # Build the subsequent breadcrumbs dynamically
                for i, part in enumerate(parts):
                    current_path += f"/{part}"
                    # Format names nicely (e.g. 'case-studies' -> 'Case Studies')
                    page_name = part.replace("-", " ").title()
                    items.append(f'{{ "@type": "ListItem", "position": {i + 2}, "name": "{page_name}", "item": "https://xsotec.com{current_path}/" }}')
                
                # Join the items list with a comma and newline for clean JSON formatting
                items_str = ",\n              ".join(items)
                
                breadcrumb_json = f"""{{
            "@type": "BreadcrumbList",
            "@id": "{url_path}#breadcrumb",
            "itemListElement": [
              {items_str}
            ]
          }}"""

            # Target the exact breadcrumb block in your newHead string to replace it
            old_breadcrumb = """{
            "@type": "BreadcrumbList",
            "@id": "/#breadcrumb",
            "itemListElement": [
              { "@type": "ListItem", "position": 1, "name": "Home" }
            ]
          }"""
            custom_head = custom_head.replace(old_breadcrumb, breadcrumb_json)

            # Inject the customized head into the HTML content
            htmlContent = htmlContent.replace(head, custom_head)

        # -- FOOTER --
        # footerFirstLine = "</main>"
        # footerLastLine = """<script type="speculationrules">"""
        # if footerFirstLine in htmlContent and footerLastLine in htmlContent:
        #     footer = footerFirstLine + htmlContent.split(footerFirstLine)[1].split(footerLastLine)[0]
        #     htmlContent = htmlContent.replace(footer, newFooter)

    with open(fileName, "w", encoding="utf-8") as file:
        file.write(htmlContent)




def prompt_for_field(label, current_value):
    """Displays the current value and prompts the user for a new one.
    Returns the new input, or the current value if the user presses ENTER."""
    print(f"\n--- {label} ---")
    print(f"Current: {current_value if current_value else '[EMPTY]'}")
    user_input = input("New Value (Press ENTER to keep current): ").strip()
    return user_input if user_input else current_value

def process_html_file(filepath):
    """Reads an HTML file, interactively prompts for metadata, and saves changes."""
    print("\n" + "=" * 80)
    print(f" EDITING FILE: {filepath}")
    print("=" * 80)

    with open(filepath, "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f, "html.parser")

    # -------------------------------------------------------------------------
    # 1. PAGE TITLE (<title>)
    # -------------------------------------------------------------------------
    title_tag = soup.find("title")
    current_title = title_tag.string.strip() if (title_tag and title_tag.string) else ""
    new_title = prompt_for_field("Page Title (<title>)", current_title)
    if title_tag:
        title_tag.string = new_title

    # -------------------------------------------------------------------------
    # 2. META DESCRIPTION (<meta name="description">)
    # -------------------------------------------------------------------------
    meta_desc = soup.find("meta", attrs={"name": "description"})
    current_desc = meta_desc["content"].strip() if (meta_desc and meta_desc.get("content")) else ""
    new_desc = prompt_for_field("Meta Description (Search Engines)", current_desc)
    if meta_desc:
        meta_desc["content"] = new_desc

    # -------------------------------------------------------------------------
    # 3. OPEN GRAPH TITLE (<meta property="og:title">)
    # -------------------------------------------------------------------------
    og_title = soup.find("meta", property="og:title")
    current_og_title = og_title["content"].strip() if (og_title and og_title.get("content")) else new_title
    new_og_title = prompt_for_field("Open Graph Title (og:title)", current_og_title)
    if og_title:
        og_title["content"] = new_og_title

    # -------------------------------------------------------------------------
    # 4. OPEN GRAPH DESCRIPTION (<meta property="og:description">)
    # -------------------------------------------------------------------------
    og_desc = soup.find("meta", property="og:description")
    current_og_desc = og_desc["content"].strip() if (og_desc and og_desc.get("content")) else new_desc
    new_og_desc = prompt_for_field("Open Graph Description (og:description)", current_og_desc)
    if og_desc:
        og_desc["content"] = new_og_desc

    # -------------------------------------------------------------------------
    # 5. OPEN GRAPH IMAGE (<meta property="og:image">)
    # -------------------------------------------------------------------------
    og_img = soup.find("meta", property="og:image")
    current_og_img = og_img["content"].strip() if (og_img and og_img.get("content")) else ""
    new_og_img = prompt_for_field("Open Graph / Feature Image Path (og:image)", current_og_img)
    if og_img:
        og_img["content"] = new_og_img

    # -------------------------------------------------------------------------
    # 6. JSON-LD SCHEMA GRAPH (YOAST SYNCHRONIZATION)
    # -------------------------------------------------------------------------
    schema_script = soup.find("script", type="application/ld+json", class_="yoast-schema-graph")
    if schema_script and schema_script.string:
        try:
            schema_data = json.loads(schema_script.string)
            if "@graph" in schema_data:
                for item in schema_data["@graph"]:
                    # Update WebPage metadata
                    if item.get("@type") == "WebPage":
                        item["name"] = new_title
                        item["description"] = new_desc
                        if new_og_img:
                            item["thumbnailUrl"] = new_og_img
                    
                    # Update ImageObject if primary image reference exists
                    elif item.get("@type") == "ImageObject" and item.get("@id", "").endswith("#primaryimage"):
                        if new_og_img:
                            item["url"] = new_og_img
                            item["contentUrl"] = new_og_img

            schema_script.string = json.dumps(schema_data, indent=2)
        except Exception as e:
            print(f"[Warning] Could not parse/update JSON-LD Schema: {e}")

    # Write changes back to the HTML file
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(str(soup))

    print(f"\n[✓] Successfully updated: {filepath}\n")

def run_meta_interactive():
    file_paths = []
    
    # Collect all HTML files
    for root, _, files in os.walk(DIRECTORY):
        for file in files:
            if file.endswith(EXTENSION):
                file_paths.append(os.path.join(root, file))

    total_files = len(file_paths)
    print(f"Found {total_files} HTML file(s) to review.")

    for idx, filepath in enumerate(file_paths, start=1):
        print(f"\nProgress: File {idx} of {total_files}")
        process_html_file(filepath)

    print("\n" + "=" * 80)
    print(" ALL FILES HAVE BEEN PROCESSED AND UPDATED!")
    print("=" * 80)


def update_modified_times(DIRECTORY=".", EXTENSION=".html"):
    # Generate the current UTC timestamp in ISO 8601 format (e.g., "2026-08-11T13:43:41+00:00")
    current_iso_time = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S+00:00")
    
    file_paths = []
    for root, _, files in os.walk(DIRECTORY):
        for file in files:
            if file.endswith(EXTENSION):
                file_paths.append(os.path.join(root, file))

    print(f"Updating modified timestamp to '{current_iso_time}' across {len(file_paths)} file(s)...\n")

    updated_count = 0

    for filepath in file_paths:
        with open(filepath, "r", encoding="utf-8") as f:
            soup = BeautifulSoup(f, "html.parser")

        file_changed = False

        # 1. Update <meta property="article:modified_time" content="..." />
        meta_modified = soup.find("meta", property="article:modified_time")
        if meta_modified:
            meta_modified["content"] = current_iso_time
            file_changed = True

        # 2. Update JSON-LD Schema "dateModified"
        schema_script = soup.find("script", type="application/ld+json", class_="yoast-schema-graph")
        if schema_script and schema_script.string:
            try:
                schema_data = json.loads(schema_script.string)
                if "@graph" in schema_data:
                    for item in schema_data["@graph"]:
                        # Update dateModified wherever it exists in the schema graph
                        if "dateModified" in item:
                            item["dateModified"] = current_iso_time
                            file_changed = True

                schema_script.string = json.dumps(schema_data, indent=2)
            except Exception as e:
                print(f"[Warning] Could not parse JSON-LD in {filepath}: {e}")

        # Save back to file if changes were made
        if file_changed:
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(str(soup))
            print(f"[✓] Updated timestamp in: {filepath}")
            updated_count += 1
        else:
            print(f"[-] No modified_time meta tags found in: {filepath}")

    print("\n" + "=" * 60)
    print(f" COMPLETE: Updated {updated_count} out of {len(file_paths)} files.")
    print("=" * 60)

