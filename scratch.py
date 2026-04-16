import sys

css_content = """
/*--------------------------------------------------------------
# General - Minimalist Creative Dark Style
--------------------------------------------------------------*/
:root {
  --bg-color: #050505; 
  --bg-alt: #0a0a0a;
  --text-main: #d4d4d8;
  --text-muted: #a1a1aa;
  --text-headers: #ffffff;
  --primary: #ffffff;
  --primary-hover: #a1a1aa;
  --border-light: rgba(255, 255, 255, 0.08);
  --border-active: rgba(255, 255, 255, 0.2);
}

body {
  font-family: "Inter", sans-serif;
  color: var(--text-main);
  background-color: var(--bg-color);
  line-height: 1.7;
}

a {
  color: var(--text-main);
  transition: color 0.3s ease;
  text-decoration: underline;
  text-underline-offset: 4px;
  text-decoration-color: var(--border-light);
}

a:hover {
  color: var(--primary);
  text-decoration-color: var(--primary);
}

h1, h2, h3, h4, h5, h6 {
  font-family: "Outfit", sans-serif;
  color: var(--text-headers);
  font-weight: 500;
  letter-spacing: -0.02em;
}

/*--------------------------------------------------------------
# Back to top button
--------------------------------------------------------------*/
.back-to-top {
  position: fixed;
  display: none;
  width: 44px;
  height: 44px;
  border-radius: 50%;
  right: 20px;
  bottom: 20px;
  background: transparent;
  border: 1px solid var(--border-active);
  color: var(--primary);
  transition: all 0.3s ease;
  z-index: 99999;
}

.back-to-top i {
  font-size: 24px;
  position: absolute;
  top: 9px;
  left: 9px;
}

.back-to-top:hover {
  background: var(--primary);
  color: var(--bg-color);
}

/*--------------------------------------------------------------
# Preloader
--------------------------------------------------------------*/
#preloader {
  position: fixed;
  top: 0; left: 0; right: 0; bottom: 0;
  z-index: 9999;
  background: var(--bg-color);
}
#preloader:before {
  content: "";
  position: fixed;
  top: calc(50% - 20px); left: calc(50% - 20px);
  border: 1px solid var(--border-light);
  border-top-color: var(--primary);
  border-radius: 50%;
  width: 40px; height: 40px;
  animation: animate-preloader 1s linear infinite;
}
@keyframes animate-preloader {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}

/*--------------------------------------------------------------
# Header & Navigation
--------------------------------------------------------------*/
#header {
  position: fixed;
  top: 0; left: 0; bottom: 0;
  z-index: 9997;
  transition: all 0.5s;
  padding: 30px 15px;
  overflow-y: auto;
  border-right: 1px solid var(--border-light);
}

@media (max-width: 992px) {
  #header {
    width: 300px;
    background: var(--bg-color);
    left: -300px;
  }
}

@media (min-width: 992px) {
  #main { margin-left: 100px; }
  #hero { padding-left: 100px; }
}

.nav-menu * {
  margin: 0; padding: 0; list-style: none;
}
.nav-menu > ul > li {
  position: relative; white-space: nowrap; margin-bottom: 20px;
}
.nav-menu a {
  display: flex;
  align-items: center; justify-content: center;
  color: var(--text-muted);
  transition: 0.3s;
  font-size: 14px;
  background: transparent;
  width: 56px; height: 56px;
  border-radius: 50%;
  text-decoration: none;
  margin: 0 auto;
}
.nav-menu a i { font-size: 22px; }
.nav-menu a span { display: none; }

@media (max-width: 992px) {
  .nav-menu a { justify-content: flex-start; padding-left: 20px; width: 100%; border-radius: 0; }
  .nav-menu a span { display: inline-block; padding-left: 15px; font-family: "Outfit", sans-serif; letter-spacing: 1px;}
}

/* Hover States for Nav */
.nav-menu a:hover, .nav-menu .active > a, .nav-menu li:hover > a {
  color: var(--primary);
}

/* Mobile Nav Toggle */
.mobile-nav-toggle {
  position: fixed;
  right: 20px; top: 20px;
  z-index: 9998; background: transparent;
  border: 1px solid var(--border-light); border-radius: 50%;
  font-size: 24px; width: 44px; height: 44px; cursor: pointer; color: var(--primary); display: flex; align-items: center; justify-content: center;
}
.mobile-nav-active { overflow: hidden; }
.mobile-nav-active #header { left: 0; }

/*--------------------------------------------------------------
# Hero Section
--------------------------------------------------------------*/
#hero {
  width: 100%; height: 100vh;
  position: relative;
  background: var(--bg-color);
  display: flex; flex-direction: column; justify-content: center;
}

#hero:before {
  display: none;
}

#hero .container {
  padding: 0 10%;
}

#hero h1 {
  margin: 0; font-size: 80px; font-weight: 800; line-height: 1.1; color: var(--text-headers);
  letter-spacing: -3px;
}
#hero p {
  color: var(--text-muted); margin: 20px 0 0 0; font-size: 20px; font-family: "Outfit", sans-serif;
  font-weight: 300;
}
#hero p span { color: var(--text-main); border-bottom: 1px solid var(--border-active); padding-bottom: 2px;}
#hero .social-links { margin-top: 40px; display: flex; gap: 20px;}
#hero .social-links a {
  font-size: 20px; display: inline-block; color: var(--text-muted);
  transition: 0.3s; text-decoration: none;
}
#hero .social-links a:hover {
  color: var(--primary); transform: translateY(-2px);
}
@media (max-width: 992px) {
  #hero { text-align: left; }
  #hero h1 { font-size: 48px; letter-spacing: -1px; }
  #hero p { font-size: 18px; }
}

/*--------------------------------------------------------------
# Sections General
--------------------------------------------------------------*/
section { padding: 120px 0; overflow: hidden; border-top: 1px solid var(--border-light); }
.section-title { text-align: left; padding-bottom: 60px; }
.section-title h2 {
  font-size: 48px; font-weight: 700; margin-bottom: 20px; 
  color: var(--text-headers); letter-spacing: -1px; text-transform: none;
}
.section-title h2::before, .section-title h2::after { display: none; }
.section-title p { color: var(--text-muted); font-size: 18px; max-width: 800px;}
.section-bg { background-color: var(--bg-alt); }

/*--------------------------------------------------------------
# About
--------------------------------------------------------------*/
.about .content {
  padding: 0;
}
.about .content h3 { font-weight: 600; font-size: 32px; color: var(--text-headers); margin-bottom: 20px; letter-spacing: -1px;}
.about .content ul { list-style: none; padding: 0; margin-top: 30px; display: grid; grid-template-columns: 1fr 1fr; gap: 20px;}
.about .content ul li { display: flex; align-items: flex-start; flex-direction: column; border-top: 1px solid var(--border-light); padding-top: 15px;}
.about .content ul i { display: none; }
.about .content ul strong { display: block; font-family: "Outfit", sans-serif; font-size: 14px; text-transform: uppercase; letter-spacing: 2px; color: var(--text-muted); margin-bottom: 5px; font-weight: 500;}
@media (max-width: 768px) { .about .content ul { grid-template-columns: 1fr; } }

/*--------------------------------------------------------------
# Facts (Favorite Quotes)
--------------------------------------------------------------*/
.facts blockquote {
  font-family: "Outfit", sans-serif;
  border-left: 2px solid var(--border-active); padding-left: 30px; margin-bottom: 50px;
}
.facts blockquote p { margin-bottom: 15px; color: var(--text-headers); font-size: 24px; font-weight: 300; letter-spacing: -0.5px;}
.facts blockquote footer { color: var(--text-muted); font-size: 14px; text-transform: uppercase; letter-spacing: 2px;}

.facts .count-box {
  padding: 40px 0; margin-top: 30px; width: 100%; border-top: 1px solid var(--border-light);
  display: flex; flex-direction: column; align-items: flex-start;
}
.facts .count-box i { display: none; }
.facts .count-box span { font-size: 64px; display: block; font-weight: 700; color: var(--text-headers); font-family: "Outfit", sans-serif; line-height: 1; margin-bottom: 15px; letter-spacing: -2px;}
.facts .count-box p { font-family: "Outfit", sans-serif; font-size: 14px; text-transform: uppercase; letter-spacing: 2px; color: var(--text-muted); }

/*--------------------------------------------------------------
# Skills
--------------------------------------------------------------*/
.skills .progress {
  height: 60px; display: block; background: none; border-radius: 0; overflow: visible; margin-bottom: 20px;
}
.skills .progress .skill {
  padding: 0 0 10px 0; margin: 0; text-transform: uppercase; display: flex; justify-content: space-between;
  font-weight: 500; font-family: "Outfit", sans-serif; color: var(--text-main);
  font-size: 14px; letter-spacing: 2px;
}
.skills .progress .skill .val { font-weight: 300; color: var(--text-muted); }
.skills .progress-bar-wrap {
  background: var(--border-light); height: 1px; width: 100%;
}
.skills .progress-bar {
  height: 100%; background-color: var(--primary); transition: width 1s ease;
}

/*--------------------------------------------------------------
# Resume
--------------------------------------------------------------*/
.resume .resume-title {
  font-size: 32px; font-weight: 600; margin-top: 40px; margin-bottom: 30px; color: var(--text-headers); letter-spacing: -1px;
}
.resume .resume-item {
  padding: 0 0 40px 30px; border-left: 1px solid var(--border-light); position: relative;
}
.resume .resume-item h4 {
  line-height: 1.4; font-size: 20px; font-weight: 500;
  color: var(--text-headers); margin-bottom: 10px;
}
.resume .resume-item h5 {
  font-size: 13px; display: inline-block;
  font-weight: 400; margin-bottom: 15px; color: var(--text-muted); font-family: "Outfit", sans-serif; letter-spacing: 1px;
}
.resume .resume-item p { color: var(--text-muted); }
.resume .resume-item ul { padding-left: 20px; color: var(--text-muted); }
.resume .resume-item::before {
  content: ""; position: absolute; width: 9px; height: 9px; border-radius: 50px;
  left: -5px; top: 8px; background: var(--bg-color); border: 2px solid var(--border-active);
  transition: 0.3s;
}
.resume .resume-item:hover::before { background: var(--primary); border-color: var(--primary); }

/*--------------------------------------------------------------
# Portfolio
--------------------------------------------------------------*/
.portfolio #portfolio-flters {
  padding: 0; margin: 0 0 40px 0; list-style: none; display: flex; gap: 30px;
}
.portfolio #portfolio-flters li {
  cursor: pointer; font-size: 14px; font-weight: 500; font-family: "Outfit", sans-serif;
  text-transform: uppercase; color: var(--text-muted); transition: all 0.3s ease; letter-spacing: 2px;
  padding-bottom: 5px; border-bottom: 1px solid transparent;
}
.portfolio #portfolio-flters li:hover, .portfolio #portfolio-flters li.filter-active {
  color: var(--primary); border-bottom: 1px solid var(--primary);
}

.portfolio .portfolio-wrap {
  transition: 0.4s; position: relative; overflow: hidden; z-index: 1;
  background: var(--bg-color); margin-bottom: 30px; border-radius: 0;
}

.portfolio .portfolio-wrap img { width: 100%; transition: transform 0.6s cubic-bezier(0.16, 1, 0.3, 1); filter: grayscale(50%); opacity: 0.8;}
.portfolio .portfolio-wrap:hover img { transform: scale(1.03); filter: grayscale(0%); opacity: 1;}

.portfolio .portfolio-info {
  margin-top: 20px; padding-bottom: 20px; border-bottom: 1px solid var(--border-light);
  display: flex; justify-content: space-between; align-items: flex-end;
}
.portfolio .portfolio-wrap .portfolio-info h4 { font-size: 20px; color: var(--text-headers); font-weight: 500; margin: 0;}
.portfolio .portfolio-wrap .portfolio-info p { color: var(--text-muted); font-size: 13px; text-transform: uppercase; font-family: "Outfit", sans-serif; margin: 5px 0 0 0; letter-spacing: 1px;}
.portfolio .portfolio-wrap .portfolio-links { display: flex; gap: 15px;}
.portfolio .portfolio-wrap .portfolio-links a {
  color: var(--text-main); font-size: 20px; transition: 0.3s; text-decoration: none;
}
.portfolio .portfolio-wrap .portfolio-links a:hover {
  color: var(--primary);
}

/*--------------------------------------------------------------
# Contact
--------------------------------------------------------------*/
.contact .info {
  width: 100%; display: grid; grid-template-columns: 1fr; gap: 40px; padding-right: 40px;
}
.contact .info .address, .contact .info .email, .contact .info .phone {
  margin: 0; padding-top: 20px; border-top: 1px solid var(--border-light);
}
.contact .info i { display: none; }
.contact .info h4 { font-size: 14px; font-weight: 500; margin-bottom: 10px; color: var(--text-muted); text-transform: uppercase; letter-spacing: 2px;}
.contact .info p { margin-bottom: 0; font-size: 18px; color: var(--text-headers); font-family: "Outfit", sans-serif;}

.contact .php-email-form {
  width: 100%;
}
.contact .php-email-form input, .contact .php-email-form textarea {
  border-radius: 0; box-shadow: none; font-size: 16px; background: transparent; 
  border: none; border-bottom: 1px solid var(--border-light); color: var(--text-main);
  padding: 15px 0; margin-bottom: 20px;
}
.contact .php-email-form input:focus, .contact .php-email-form textarea:focus {
  background: transparent; border-color: var(--primary);
  color: var(--primary); outline: none; box-shadow: none;
}
.contact .php-email-form input::placeholder, .contact .php-email-form textarea::placeholder {
  color: var(--text-muted); font-weight: 300;
}
.contact .php-email-form button[type="submit"] {
  background: transparent; border: 1px solid border-light; padding: 15px 40px;
  color: var(--text-main); transition: 0.4s; border-radius: 0; font-family: "Outfit", sans-serif;
  font-weight: 500; text-transform: uppercase; letter-spacing: 2px; margin-top: 20px; font-size: 14px;
  border-bottom: 1px solid var(--text-main); display: inline-block;
}
.contact .php-email-form button[type="submit"]:hover {
  color: var(--primary); border-bottom-color: var(--primary);
}

/*--------------------------------------------------------------
# Footer
--------------------------------------------------------------*/
#footer {
  background: var(--bg-alt); color: var(--text-muted); font-size: 14px; text-align: center;
  padding: 60px 0; margin-top: 80px; border-top: 1px solid var(--border-light);
}
#footer h3 { font-size: 24px; font-weight: 600; color: var(--text-headers); letter-spacing: -0.5px;}
#footer .social-links { margin: 30px 0; display: flex; justify-content: center; gap: 20px;}
#footer .social-links a {
  font-size: 20px; color: var(--text-muted); transition: 0.3s; text-decoration: none;
}
#footer .social-links a:hover {
  color: var(--primary);
}
#footer .copyright { margin: 0; font-family: "Outfit", sans-serif;}
"""

with open('assets/css/style.css', 'w') as f:
    f.write(css_content)

print("Minimalist CSS generated.")
