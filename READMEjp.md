[English](./README.md)

# Google GenAI Agent Skillsへようこそ！ 🚀

**Google GenAI Agent Skills** リポジトリをご覧いただきありがとうございます！ ここでは、あなたのAIエージェントがGoogleのGenerative AIの強力な機能を使えるようにするためのスキルセットを提供しています。 🧠✨

**Claude Code** でも **Gemini CLI** でも、これらのスキルを使えば、あなたのワークフローに最新のAI機能を簡単に組み込むことができますよ。

---

## 📦 インストールと使い方

お使いのツールに合わせて、以下の手順でセットアップしてくださいね。とっても簡単です！ 👇

### ▲ For using `npx skills`

Agent Skillsをより簡単に使用するためのCLIツール、`npx skills`を使用してこのSkillをインストールするには、以下のコマンドをご利用ください！！

```shell
npx skills add https://github.com/yharuto0917/GoogleGenAI-AgentSkills-Python --skill google-genai
```

### 🤖 Claude Code をお使いの方

**Claude Code** でこのスキルを使うには、リポジトリをクローンして、`skills/google-genai` ディレクトリをプロジェクトの `claude` フォルダ内に配置するだけです。

1. **リポジトリをクローンします:**

    ```bash
    git clone https://github.com/YourUsername/GoogleGenAI-AgentSkills.git
    ```

2. **スキルを配置します:**
    `skills/google-genai` フォルダを、あなたのプロジェクトの `./claude/skills/google-genai` に移動してください。

    ```bash
    mkdir -p ./claude/skills
    cp -r GoogleGenAI-AgentSkills/skills/google-genai ./claude/skills/
    ```

    *これだけで、Claude Code がさらに賢くなります！* 🎉

### 💎 Gemini CLI をお使いの方

**Gemini CLI** では、スキルをプロジェクトごとに管理したり、どこからでも使えるようにしたりできます。 🌍

> **詳しくはこちら:** [Gemini CLI Skills Documentation](https://geminicli.com/docs/cli/skills/)

1. **リポジトリをクローンします:**

    ```bash
    git clone https://github.com/YourUsername/GoogleGenAI-AgentSkills.git
    ```

2. **スキルをインストールします:**
    `skills/google-genai` フォルダを、以下のいずれかの場所に配置してください。

    * **プロジェクト専用:** `.gemini/skills/` (プロジェクトのルートディレクトリ)
    * **グローバル (ユーザー全体):** `~/.gemini/skills/`

    ```bash
    # 例: グローバルにインストールする場合
    mkdir -p ~/.gemini/skills
    cp -r GoogleGenAI-AgentSkills/skills/google-genai ~/.gemini/skills/
    ```

    *これで、Gemini がGoogle GenAIの力を発揮できるようになります！* 🚀

---

## 🌟 特徴

* **シームレスな統合:** Claude Code と Gemini CLI の両方に対応しています。
* **Google GenAIのパワー:** 最新の生成AIモデルとツールを活用できます。
* **拡張も簡単:** 必要に合わせてスキルをカスタマイズすることも可能です。

Happy coding! 💻✨
