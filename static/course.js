// DARK MODE

window.addEventListener('DOMContentLoaded', event => {
    toggleTheme();
  });
  
  const toggleTheme = () => {
    // Theme toggle button.
    const toggleSwitch = document.querySelector('.theme-switch input[type="checkbox"]');
    function switchTheme(e) {
      let darkModeEnabled = e.target.checked;
      document.documentElement.setAttribute('data-theme', darkModeEnabled ? 'dark' : 'light');
      localStorage.setItem('theme', darkModeEnabled ? 'dark' : 'light');
    }
    toggleSwitch.addEventListener('change', switchTheme, false);
  
    // Restore theme state.
    const currentTheme = localStorage.getItem('theme') ? localStorage.getItem('theme') : null;
    if (currentTheme) {
      document.documentElement.setAttribute('data-theme', currentTheme);
      if (currentTheme === 'dark') {
        toggleSwitch.checked = true;
      }
    }
  }