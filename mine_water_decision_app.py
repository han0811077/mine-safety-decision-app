import streamlit as st

st.set_page_config(page_title="矿井突水应急处置决策系统", page_icon="⛑️", layout="centered")
st.title("⛑️ 矿井突水应急处置决策支持系统")
st.markdown("**请根据现场实际情况，依次回答下列问题。系统将给出应急处置建议。**")

# 初始化session_state
if 'step' not in st.session_state:
    st.session_state.step = 1
if 'decision_made' not in st.session_state:
    st.session_state.decision_made = False

def reset_form():
    st.session_state.step = 1
    st.session_state.decision_made = False

# 问题与决策逻辑
if not st.session_state.decision_made:
    if st.session_state.step == 1:
        st.subheader("第一步：初步报告")
        alarm = st.radio("是否已立即发出警报并向调度室报告？", ("是", "否"), key="step1")
        if alarm == "是":
            st.session_state.step = 2
            st.rerun()
        else:
            st.error("❌ **首要行动：请立即发出警报并报告调度室！** 这是所有应急处置的第一步。")
            
    elif st.session_state.step == 2:
        st.subheader("第二步：险情评估")
        urgency = st.radio("突水征兆是否正在急剧变化？（例如：水量猛增、巷道顶板/底板变形加速、闻到臭鸡蛋味等）", ("是", "否"), key="step2")
        if urgency == "是":
            st.session_state.final_decision = "🚨 **【紧急决策：立即撤离】** 🚨\n\n**行动建议：**\n1. 立即停止所有作业。\n2. 沿预先确定的避灾路线，组织所有人员迅速撤离。\n3. 撤离时注意相互照应，告知可能受威胁区域的人员。\n4. 随时向调度室报告位置和情况。\n\n**原则：生命至上，无需犹豫。**"
            st.session_state.decision_made = True
        else:
            st.session_state.step = 3
            st.rerun()

    elif st.session_state.step == 3:
        st.subheader("第三步：水源与位置判断")
        high_risk = st.radio("水源是否疑似为老空水，或者作业人员是否位于透水危险区域的下方？", ("是", "否"), key="step3")
        if high_risk == "是":
            st.session_state.final_decision = "⚠️ **【高风险决策：预防性撤离】** ⚠️\n\n**行动建议：**\n1. 立即停止作业，切断工作面电源。\n2. 所有人员立即撤离至安全区域。\n3. 老空水可能伴有硫化氢等有害气体，风险极高。\n4. 等待进一步勘查和指令。"
            st.session_state.decision_made = True
        else:
            st.session_state.step = 4
            st.rerun()

    elif st.session_state.step == 4:
        st.subheader("第四步：应急能力评估")
        capable = st.radio("现场是否有经验、有材料、有设备，且在水情稳定、确保安全的前提下，能够进行有效的临时加固或导水作业？", ("是", "否"), key="step4")
        if capable == "是":
            st.session_state.final_decision = "🛠️ **【决策：可控应急处置】** 🛠️\n\n**行动建议：**\n1. 在跟班队长或技术人员的指挥下进行。\n2. 安排专人观测水情和顶板情况。\n3. 采取打设点柱、构筑防水闸墙等措施。\n4. 一旦情况恶化，立即停止作业并撤离。"
            st.session_state.decision_made = True
        else:
            st.session_state.final_decision = "🟡 **【决策：警戒待援】** 🟡\n\n**行动建议：**\n1. 立即停止作业，人员撤至安全地点。\n2. 在危险区域设置明显的警戒线和警示牌。\n3. 持续监测水情变化。\n4. 等待专业救护队和指挥部进一步的勘查与指令。**严禁盲目施救！**"
            st.session_state.decision_made = True

# 显示最终决策
if st.session_state.decision_made:
    st.success(st.session_state.final_decision)
    st.button("重新开始决策模拟", on_click=reset_form)

# 侧边栏信息
with st.sidebar:
    st.header("应急处置原则")
    st.markdown("""
    - **安全第一**：生命高于一切。
    - **及时报告**：任何征兆都必须立即上报。
    - **先撤人后处置**：在情况不明或风险较高时，优先保证人员安全。
    - **科学施救**：杜绝盲目行动。
    """)
    st.header("常见突水征兆")
    st.markdown("""
    - 巷道壁"挂汗"、渗水
    - 淋水加大，如"下雨"
    - 水叫声、水吼声
    - 顶板来压、底板鼓起
    - 水色发浑、有异味
    - 工作面温度下降
    """)