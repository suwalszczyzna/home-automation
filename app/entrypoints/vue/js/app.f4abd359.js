(function(){var e={133:function(e,t,n){"use strict";var r=n(963),o=n(974),a=n(252);const i={id:"app"};function u(e,t,n,r,o,u){const s=(0,a.up)("router-view"),c=(0,a.up)("AppLayout");return(0,a.wg)(),(0,a.iD)("div",i,[(0,a.Wm)(c,null,{default:(0,a.w5)((()=>[(0,a.Wm)(s)])),_:1})])}var s=n(234),c={name:"App",components:{AppLayout:s["default"]}},l=n(744);const f=(0,l.Z)(c,[["render",u]]);var d=f,p=n(205);(0,p.z)("/service-worker.js",{ready(){console.log("App is being served from cache by a service worker.\nFor more details, visit https://goo.gl/AFskqB")},registered(){console.log("Service worker has been registered.")},cached(){console.log("Content has been cached for offline use.")},updatefound(){console.log("New content is downloading.")},updated(){console.log("New content is available; please refresh.")},offline(){console.log("No internet connection found. App is running in offline mode.")},error(e){console.error("Error during service worker registration:",e)}});var v=n(119);const m=[{path:"/settings",name:"Settings",component:()=>n.e(13).then(n.bind(n,13))},{path:"/",name:"Home",component:()=>n.e(270).then(n.bind(n,270))}],g=(0,v.p7)({history:(0,v.PO)("/"),routes:m});var h=g;(0,r.ri)(d).use((0,o.WB)()).use(h).mount("#app")},234:function(e,t,n){"use strict";n.r(t),n.d(t,{default:function(){return f}});var r=n(252);function o(e,t,n,o,a,i){return(0,r.wg)(),(0,r.j4)((0,r.LL)(o.layout),null,{default:(0,r.w5)((()=>[(0,r.WI)(e.$slots,"default")])),_:3})}var a=n(899),i=n(262),u=n(119),s={name:"AppLayout",setup(){const e=(0,i.Xl)(a["default"]),t=(0,u.yj)();return(0,r.YP)((()=>t.meta),(async t=>{try{const r=await n(115)(`./${t.layout}.vue`);e.value=r?.default||a["default"]}catch(r){e.value=a["default"]}}),{immediate:!0}),{layout:e}}},c=n(744);const l=(0,c.Z)(s,[["render",o]]);var f=l},899:function(e,t,n){"use strict";n.r(t),n.d(t,{default:function(){return d}});var r=n(252);const o={class:"container mx-auto min-h-screen"},a={class:"p-4 container mx-auto max-w-screen-sm"};function i(e,t,n,i,u,s){const c=(0,r.up)("AppTopNavbar"),l=(0,r.up)("AppLayoutNavbar");return(0,r.wg)(),(0,r.iD)("div",o,[(0,r.Wm)(c),(0,r.Wm)(l),(0,r._)("div",a,[(0,r.WI)(e.$slots,"default")])])}var u=n(240),s=n(597),c={name:"AppLayoutDefault",components:{AppLayoutNavbar:u["default"],AppTopNavbar:s["default"]}},l=n(744);const f=(0,l.Z)(c,[["render",i]]);var d=f},240:function(e,t,n){"use strict";n.r(t),n.d(t,{default:function(){return v}});var r=n(252);const o={class:"fixed bottom-0 inset-x-0 bg-gray-100 border-t-2 border-gray-200"},a={class:"mx-auto max-w-screen-sm flex justify-between text-sm text-gray-900 uppercase font-mono"},i=(0,r._)("svg",{xmlns:"http://www.w3.org/2000/svg",class:"w-6 h-6 mb-2 mx-auto",fill:"none",viewBox:"0 0 24 24",stroke:"currentColor"},[(0,r._)("path",{"stroke-linecap":"round","stroke-linejoin":"round","stroke-width":"2",d:"M3 12l2-2m0 0l7-7 7 7M5 10v10a1 1 0 001 1h3m10-11l2 2m-2-2v10a1 1 0 01-1 1h-3m-6 0a1 1 0 001-1v-4a1 1 0 011-1h2a1 1 0 011 1v4a1 1 0 001 1m-6 0h6"})],-1),u=(0,r.Uk)(" Home "),s=(0,r._)("svg",{class:"w-6 h-6 mb-2 mx-auto",xmlns:"http://www.w3.org/2000/svg",fill:"none",viewBox:"0 0 24 24",stroke:"currentColor"},[(0,r._)("path",{"stroke-linecap":"round","stroke-linejoin":"round","stroke-width":"2",d:"M12 6V4m0 2a2 2 0 100 4m0-4a2 2 0 110 4m-6 8a2 2 0 100-4m0 4a2 2 0 110-4m0 4v2m0-6V4m6 6v10m6-2a2 2 0 100-4m0 4a2 2 0 110-4m0 4v2m0-6V4"})],-1),c=(0,r.Uk)(" Ustawienia ");function l(e,t,n,l,f,d){const p=(0,r.up)("router-link");return(0,r.wg)(),(0,r.iD)("div",o,[(0,r._)("nav",a,[(0,r.Wm)(p,{to:"/",class:"w-full block py-3 px-3 text-center hover:bg-gray-200 hover:text-gray-800 transition duration-300"},{default:(0,r.w5)((()=>[i,u])),_:1}),(0,r.Wm)(p,{to:"/settings",class:"w-full block py-3 px-3 text-center hover:bg-gray-200 hover:text-gray-800"},{default:(0,r.w5)((()=>[s,c])),_:1})])])}var f={name:"AppLayoutNavbar"},d=n(744);const p=(0,d.Z)(f,[["render",l]]);var v=p},597:function(e,t,n){"use strict";n.r(t),n.d(t,{default:function(){return f}});var r=n(252);const o={class:"bg-gray-100 border-b-2 border-gray-200"},a=(0,r.uE)('<nav class="p-4 container mx-auto max-w-screen-sm flex items-center justify-between flex-wrap"><div class="flex items-center flex-shrink-0 text-grey mr-6"><svg class="fill-current h-8 w-8 mr-2" width="54" height="54" viewBox="0 0 54 54" xmlns="http://www.w3.org/2000/svg"><path d="M13.5 22.1c1.8-7.2 6.3-10.8 13.5-10.8 10.8 0 12.15 8.1 17.55 9.45 3.6.9 6.75-.45 9.45-4.05-1.8 7.2-6.3 10.8-13.5 10.8-10.8 0-12.15-8.1-17.55-9.45-3.6-.9-6.75.45-9.45 4.05zM0 38.3c1.8-7.2 6.3-10.8 13.5-10.8 10.8 0 12.15 8.1 17.55 9.45 3.6.9 6.75-.45 9.45-4.05-1.8 7.2-6.3 10.8-13.5 10.8-10.8 0-12.15-8.1-17.55-9.45-3.6-.9-6.75.45-9.45 4.05z"></path></svg><span class="font-semibold text-xl tracking-tight">Home automation</span></div></nav>',1),i=[a];function u(e,t,n,a,u,s){return(0,r.wg)(),(0,r.iD)("div",o,i)}var s={name:"AppTopNavbar"},c=n(744);const l=(0,c.Z)(s,[["render",u]]);var f=l},115:function(e,t,n){var r={"./AppLayout.vue":234,"./AppLayoutDefault.vue":899,"./AppLayoutNavbar.vue":240,"./AppTopNavbar.vue":597};function o(e){return Promise.resolve().then((function(){if(!n.o(r,e)){var t=new Error("Cannot find module '"+e+"'");throw t.code="MODULE_NOT_FOUND",t}var o=r[e];return n(o)}))}o.keys=function(){return Object.keys(r)},o.id=115,e.exports=o}},t={};function n(r){var o=t[r];if(void 0!==o)return o.exports;var a=t[r]={exports:{}};return e[r](a,a.exports,n),a.exports}n.m=e,function(){var e=[];n.O=function(t,r,o,a){if(!r){var i=1/0;for(l=0;l<e.length;l++){r=e[l][0],o=e[l][1],a=e[l][2];for(var u=!0,s=0;s<r.length;s++)(!1&a||i>=a)&&Object.keys(n.O).every((function(e){return n.O[e](r[s])}))?r.splice(s--,1):(u=!1,a<i&&(i=a));if(u){e.splice(l--,1);var c=o();void 0!==c&&(t=c)}}return t}a=a||0;for(var l=e.length;l>0&&e[l-1][2]>a;l--)e[l]=e[l-1];e[l]=[r,o,a]}}(),function(){n.d=function(e,t){for(var r in t)n.o(t,r)&&!n.o(e,r)&&Object.defineProperty(e,r,{enumerable:!0,get:t[r]})}}(),function(){n.f={},n.e=function(e){return Promise.all(Object.keys(n.f).reduce((function(t,r){return n.f[r](e,t),t}),[]))}}(),function(){n.u=function(e){return"js/"+e+"."+{13:"62e1663a",270:"852947c4"}[e]+".js"}}(),function(){n.miniCssF=function(e){}}(),function(){n.g=function(){if("object"===typeof globalThis)return globalThis;try{return this||new Function("return this")()}catch(e){if("object"===typeof window)return window}}()}(),function(){n.o=function(e,t){return Object.prototype.hasOwnProperty.call(e,t)}}(),function(){var e={},t="home-automation-gui:";n.l=function(r,o,a,i){if(e[r])e[r].push(o);else{var u,s;if(void 0!==a)for(var c=document.getElementsByTagName("script"),l=0;l<c.length;l++){var f=c[l];if(f.getAttribute("src")==r||f.getAttribute("data-webpack")==t+a){u=f;break}}u||(s=!0,u=document.createElement("script"),u.charset="utf-8",u.timeout=120,n.nc&&u.setAttribute("nonce",n.nc),u.setAttribute("data-webpack",t+a),u.src=r),e[r]=[o];var d=function(t,n){u.onerror=u.onload=null,clearTimeout(p);var o=e[r];if(delete e[r],u.parentNode&&u.parentNode.removeChild(u),o&&o.forEach((function(e){return e(n)})),t)return t(n)},p=setTimeout(d.bind(null,void 0,{type:"timeout",target:u}),12e4);u.onerror=d.bind(null,u.onerror),u.onload=d.bind(null,u.onload),s&&document.head.appendChild(u)}}}(),function(){n.r=function(e){"undefined"!==typeof Symbol&&Symbol.toStringTag&&Object.defineProperty(e,Symbol.toStringTag,{value:"Module"}),Object.defineProperty(e,"__esModule",{value:!0})}}(),function(){n.p="/"}(),function(){var e={143:0};n.f.j=function(t,r){var o=n.o(e,t)?e[t]:void 0;if(0!==o)if(o)r.push(o[2]);else{var a=new Promise((function(n,r){o=e[t]=[n,r]}));r.push(o[2]=a);var i=n.p+n.u(t),u=new Error,s=function(r){if(n.o(e,t)&&(o=e[t],0!==o&&(e[t]=void 0),o)){var a=r&&("load"===r.type?"missing":r.type),i=r&&r.target&&r.target.src;u.message="Loading chunk "+t+" failed.\n("+a+": "+i+")",u.name="ChunkLoadError",u.type=a,u.request=i,o[1](u)}};n.l(i,s,"chunk-"+t,t)}},n.O.j=function(t){return 0===e[t]};var t=function(t,r){var o,a,i=r[0],u=r[1],s=r[2],c=0;if(i.some((function(t){return 0!==e[t]}))){for(o in u)n.o(u,o)&&(n.m[o]=u[o]);if(s)var l=s(n)}for(t&&t(r);c<i.length;c++)a=i[c],n.o(e,a)&&e[a]&&e[a][0](),e[a]=0;return n.O(l)},r=self["webpackChunkhome_automation_gui"]=self["webpackChunkhome_automation_gui"]||[];r.forEach(t.bind(null,0)),r.push=t.bind(null,r.push.bind(r))}();var r=n.O(void 0,[998],(function(){return n(133)}));r=n.O(r)})();
//# sourceMappingURL=app.f4abd359.js.map