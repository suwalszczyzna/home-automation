(function(e){function t(t){for(var r,c,u=t[0],i=t[1],s=t[2],l=0,d=[];l<u.length;l++)c=u[l],Object.prototype.hasOwnProperty.call(o,c)&&o[c]&&d.push(o[c][0]),o[c]=0;for(r in i)Object.prototype.hasOwnProperty.call(i,r)&&(e[r]=i[r]);f&&f(t);while(d.length)d.shift()();return a.push.apply(a,s||[]),n()}function n(){for(var e,t=0;t<a.length;t++){for(var n=a[t],r=!0,c=1;c<n.length;c++){var i=n[c];0!==o[i]&&(r=!1)}r&&(a.splice(t--,1),e=u(u.s=n[0]))}return e}var r={},o={app:0},a=[];function c(e){return u.p+"js/"+({}[e]||e)+"."+{"chunk-133ac899":"70216205","chunk-2d0b3289":"c5e6dba3"}[e]+".js"}function u(t){if(r[t])return r[t].exports;var n=r[t]={i:t,l:!1,exports:{}};return e[t].call(n.exports,n,n.exports,u),n.l=!0,n.exports}u.e=function(e){var t=[],n=o[e];if(0!==n)if(n)t.push(n[2]);else{var r=new Promise((function(t,r){n=o[e]=[t,r]}));t.push(n[2]=r);var a,i=document.createElement("script");i.charset="utf-8",i.timeout=120,u.nc&&i.setAttribute("nonce",u.nc),i.src=c(e);var s=new Error;a=function(t){i.onerror=i.onload=null,clearTimeout(l);var n=o[e];if(0!==n){if(n){var r=t&&("load"===t.type?"missing":t.type),a=t&&t.target&&t.target.src;s.message="Loading chunk "+e+" failed.\n("+r+": "+a+")",s.name="ChunkLoadError",s.type=r,s.request=a,n[1](s)}o[e]=void 0}};var l=setTimeout((function(){a({type:"timeout",target:i})}),12e4);i.onerror=i.onload=a,document.head.appendChild(i)}return Promise.all(t)},u.m=e,u.c=r,u.d=function(e,t,n){u.o(e,t)||Object.defineProperty(e,t,{enumerable:!0,get:n})},u.r=function(e){"undefined"!==typeof Symbol&&Symbol.toStringTag&&Object.defineProperty(e,Symbol.toStringTag,{value:"Module"}),Object.defineProperty(e,"__esModule",{value:!0})},u.t=function(e,t){if(1&t&&(e=u(e)),8&t)return e;if(4&t&&"object"===typeof e&&e&&e.__esModule)return e;var n=Object.create(null);if(u.r(n),Object.defineProperty(n,"default",{enumerable:!0,value:e}),2&t&&"string"!=typeof e)for(var r in e)u.d(n,r,function(t){return e[t]}.bind(null,r));return n},u.n=function(e){var t=e&&e.__esModule?function(){return e["default"]}:function(){return e};return u.d(t,"a",t),t},u.o=function(e,t){return Object.prototype.hasOwnProperty.call(e,t)},u.p="/",u.oe=function(e){throw console.error(e),e};var i=window["webpackJsonp"]=window["webpackJsonp"]||[],s=i.push.bind(i);i.push=t,i=i.slice();for(var l=0;l<i.length;l++)t(i[l]);var f=s;a.push([0,"chunk-vendors"]),n()})({0:function(e,t,n){e.exports=n("cd49")},"266e":function(e,t,n){"use strict";n.r(t);var r=n("7a23"),o={class:"container mx-auto min-h-screen font-light p-2"};function a(e,t,n,a,c,u){var i=Object(r["x"])("AppLayoutNavbar");return Object(r["s"])(),Object(r["d"])("div",o,[Object(r["g"])(i),Object(r["w"])(e.$slots,"default")])}var c=n("35b4"),u={name:"AppLayoutDefault",components:{AppLayoutNavbar:c["default"]}},i=n("6b0d"),s=n.n(i);const l=s()(u,[["render",a]]);t["default"]=l},"35b4":function(e,t,n){"use strict";n.r(t);var r=n("7a23"),o={class:"fixed bottom-0 inset-x-0 bg-gray-100 flex justify-between text-sm text-gray-900 uppercase font-mono"},a=Object(r["e"])("svg",{xmlns:"http://www.w3.org/2000/svg",class:"w-6 h-6 mb-2 mx-auto",fill:"none",viewBox:"0 0 24 24",stroke:"currentColor"},[Object(r["e"])("path",{"stroke-linecap":"round","stroke-linejoin":"round","stroke-width":"2",d:"M3 12l2-2m0 0l7-7 7 7M5 10v10a1 1 0 001 1h3m10-11l2 2m-2-2v10a1 1 0 01-1 1h-3m-6 0a1 1 0 001-1v-4a1 1 0 011-1h2a1 1 0 011 1v4a1 1 0 001 1m-6 0h6"})],-1),c=Object(r["f"])(" Home "),u=Object(r["e"])("svg",{class:"w-6 h-6 mb-2 mx-auto",xmlns:"http://www.w3.org/2000/svg",fill:"none",viewBox:"0 0 24 24",stroke:"currentColor"},[Object(r["e"])("path",{"stroke-linecap":"round","stroke-linejoin":"round","stroke-width":"2",d:"M12 6V4m0 2a2 2 0 100 4m0-4a2 2 0 110 4m-6 8a2 2 0 100-4m0 4a2 2 0 110-4m0 4v2m0-6V4m6 6v10m6-2a2 2 0 100-4m0 4a2 2 0 110-4m0 4v2m0-6V4"})],-1),i=Object(r["f"])(" Ustawienia ");function s(e,t,n,s,l,f){var d=Object(r["x"])("router-link");return Object(r["s"])(),Object(r["d"])("nav",o,[Object(r["g"])(d,{to:"/",class:"w-full block py-3 px-3 text-center hover:bg-gray-200 hover:text-gray-800 transition duration-300"},{default:Object(r["D"])((function(){return[a,c]})),_:1}),Object(r["g"])(d,{to:"/settings",class:"w-full block py-3 px-3 text-center hover:bg-gray-200 hover:text-gray-800"},{default:Object(r["D"])((function(){return[u,i]})),_:1})])}var l={name:"AppLayoutNavbar"},f=n("6b0d"),d=n.n(f);const p=d()(l,[["render",s]]);t["default"]=p},a449:function(e,t,n){var r={"./AppLayout.vue":"dead","./AppLayoutDefault.vue":"266e","./AppLayoutNavbar.vue":"35b4"};function o(e){return Promise.resolve().then((function(){if(!n.o(r,e)){var t=new Error("Cannot find module '"+e+"'");throw t.code="MODULE_NOT_FOUND",t}var o=r[e];return n(o)}))}o.keys=function(){return Object.keys(r)},o.id="a449",e.exports=o},ba8c:function(e,t,n){},cd49:function(e,t,n){"use strict";n.r(t);n("e260"),n("e6cf"),n("cca6"),n("a79d");var r=n("7a23"),o={id:"app"};function a(e,t,n,a,c,u){var i=Object(r["x"])("router-view"),s=Object(r["x"])("AppLayout");return Object(r["s"])(),Object(r["d"])("div",o,[Object(r["g"])(s,null,{default:Object(r["D"])((function(){return[Object(r["g"])(i)]})),_:1})])}var c=n("dead"),u={name:"App",components:{AppLayout:c["default"]}},i=n("6b0d"),s=n.n(i);const l=s()(u,[["render",a]]);var f=l,d=n("9483");Object(d["a"])("".concat("/","service-worker.js"),{ready:function(){console.log("App is being served from cache by a service worker.\nFor more details, visit https://goo.gl/AFskqB")},registered:function(){console.log("Service worker has been registered.")},cached:function(){console.log("Content has been cached for offline use.")},updatefound:function(){console.log("New content is downloading.")},updated:function(){console.log("New content is available; please refresh.")},offline:function(){console.log("No internet connection found. App is running in offline mode.")},error:function(e){console.error("Error during service worker registration:",e)}});n("d3b7"),n("3ca3"),n("ddb0");var p=n("6c02"),b=[{path:"/",name:"Home",component:function(){return n.e("chunk-133ac899").then(n.bind(null,"bb51"))}},{path:"/settings",name:"Settings",component:function(){return n.e("chunk-2d0b3289").then(n.bind(null,"26d3"))}}],v=Object(p["a"])({history:Object(p["b"])("/"),routes:b}),m=v;Object(r["b"])(f).use(m).mount("#app")},dead:function(e,t,n){"use strict";n.r(t);var r=n("7a23");function o(e,t,n,o,a,c){return Object(r["s"])(),Object(r["c"])(Object(r["y"])(o.layout),null,{default:Object(r["D"])((function(){return[Object(r["w"])(e.$slots,"default")]})),_:3})}var a=n("1da1"),c=(n("96cf"),n("d3b7"),n("3ca3"),n("ddb0"),n("266e")),u=n("6c02"),i=(n("ba8c"),{name:"AppLayout",setup:function(){var e=Object(r["l"])(c["default"]),t=Object(u["c"])();return Object(r["C"])((function(){return t.meta}),function(){var t=Object(a["a"])(regeneratorRuntime.mark((function t(r){var o;return regeneratorRuntime.wrap((function(t){while(1)switch(t.prev=t.next){case 0:return t.prev=0,t.next=3,n("a449")("./".concat(r.layout,".vue"));case 3:o=t.sent,e.value=(null===o||void 0===o?void 0:o.default)||c["default"],t.next=10;break;case 7:t.prev=7,t.t0=t["catch"](0),e.value=c["default"];case 10:case"end":return t.stop()}}),t,null,[[0,7]])})));return function(e){return t.apply(this,arguments)}}(),{immediate:!0}),{layout:e}}}),s=n("6b0d"),l=n.n(s);const f=l()(i,[["render",o]]);t["default"]=f}});
//# sourceMappingURL=app.83da2205.js.map