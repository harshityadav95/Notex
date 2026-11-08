/* Set the stored preference before CSS paints. Light remains the default. */
(()=>{'use strict';let theme='light';try{if(localStorage.getItem('notex-theme')==='dark')theme='dark';}catch{}document.documentElement.dataset.theme=theme;})();
