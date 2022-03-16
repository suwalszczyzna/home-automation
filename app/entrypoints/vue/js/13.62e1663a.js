"use strict";(self["webpackChunkhome_automation_gui"]=self["webpackChunkhome_automation_gui"]||[]).push([[13],{13:function(e,o,t){t.r(o),t.d(o,{default:function(){return H}});var a=t(252);const n=(0,a._)("h2",{class:"text-xl"},"Ustawienia",-1);function i(e,o,t,i,s,u){const l=(0,a.up)("OperationModes");return(0,a.wg)(),(0,a.iD)("div",null,[n,(0,a._)("div",null,[(0,a.Wm)(l)])])}var s=t(577),u=t(963);const l={key:0,class:"flex items-center justify-center"},r=(0,a._)("h1",null,"Ładowanie...",-1),c=[r],d={key:1,class:"p-2 mt-2"},h={class:"inline-flex shadow-md hover:shadow-lg focus:shadow-lg",role:"group"},g={class:"mt-3 flex items-center"},v={class:"flex items-center cursor-pointer"},p=["checked"],_=(0,a._)("span",{class:"ml-2"},"Zwracaj uwagę na drugą taryfę",-1);function f(e,o,t,n,i,r){return e.isLoading?((0,a.wg)(),(0,a.iD)("div",l,c)):((0,a.wg)(),(0,a.iD)("div",d,[((0,a.wg)(),(0,a.iD)("div",{class:"flex items-center",key:e.key},[(0,a._)("div",h,[(0,a._)("a",{onClick:o[0]||(o[0]=o=>e.changeOperationMode("auto_mode")),class:(0,s.C_)(["cursor-pointer rounded-l px-6 py-2.5 bg-gray-400 text-white font-medium text-xs leading-tight uppercase hover:bg-blue-700 focus:bg-blue-700 focus:outline-none focus:ring-0 transition duration-150 ease-in-out",{"bg-blue-900":e.isAutoMode}])}," Pełna automatyka ",2),(0,a._)("a",{onClick:o[1]||(o[1]=o=>e.changeOperationMode("auto_mode_heater")),class:(0,s.C_)(["cursor-pointer rounded-r px-6 py-2.5 bg-gray-400 text-white font-medium text-xs leading-tight uppercase hover:bg-blue-700 focus:bg-blue-700 focus:outline-none focus:ring-0 transition duration-150 ease-in-out",{"bg-blue-900":e.isHeaterMode}])}," Tylko grzałka ",2)])])),(0,a._)("div",g,[(0,a._)("label",v,[(0,a.wy)((0,a._)("input",{onChange:o[2]||(o[2]=o=>e.lowCostChecking()),checked:e.isLowCostHeater,"onUpdate:modelValue":o[3]||(o[3]=o=>e.isLowCostHeater=o),type:"checkbox",class:"form-checkbox"},null,40,p),[[u.e8,e.isLowCostHeater]]),_])])]))}var m=t(262),w=(0,a.aZ)({name:"OperationModes",setup(){const e=(0,m.iH)(0),o=(0,m.iH)(""),t=(0,m.iH)(!1),n=(0,m.iH)(!0),i=(0,m.iH)(!1),s=(0,m.iH)(!1);function u(){n.value=!0;const e=`http://192.168.1.25:5000/api/set_checking_low_cost?operation=${o.value}&value=${t.value}`;fetch(e).then((e=>e.json())).then((e=>{console.log(e)})).catch((e=>{console.error(e)})).finally((()=>{n.value=!1}))}function l(e){const o=`http://192.168.1.25:5000/api/set_operation_mode?operation=${e}`;n.value=!0,fetch(o).then((e=>e.json())).then((e=>{console.log(e)})).catch((e=>console.error(e))).finally((()=>{n.value=!1}))}function r(){n.value=!0,fetch("http://192.168.1.25:5000/api/get_actual_mode").then((e=>e.json())).then((e=>{console.log(e),o.value=e.operation_mode,t.value=e.heater_on_lower_cost_only,n.value=!1,"auto_mode"==o.value?(i.value=!0,s.value=!1):"auto_mode_heater"==o.value&&(i.value=!1,s.value=!0)})).catch((e=>{console.error(e),n.value=!1}))}function c(e){"auto_mode"==e?(i.value=!0,s.value=!1,o.value=e):"auto_mode_heater"==e&&(i.value=!1,s.value=!0,o.value=e),l(o.value),setTimeout((()=>r()),500)}return(0,a.bv)((()=>{r()})),{key:e,operationMode:o,isLowCostHeater:t,isLoading:n,isAutoMode:i,isHeaterMode:s,lowCostChecking:u,changeOperationMode:c}}}),k=t(744);const b=(0,k.Z)(w,[["render",f]]);var y=b,x=(0,a.aZ)({name:"SettingsView",components:{OperationModes:y}});const C=(0,k.Z)(x,[["render",i]]);var H=C}}]);
//# sourceMappingURL=13.62e1663a.js.map