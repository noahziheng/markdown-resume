---
title: 高梓恒 - 系统与平台工程师
author: Noah Gao
lang: zh-CN
description: 高梓恒的简历 - 系统与平台工程师，关注 Agent 基础设施
---

# 高梓恒（Noah Gao）

**系统与平台工程师 · 7 年经验 · 北京**

做过云 IDE 的工作区基建，也做过 AI IDE 里的 Agent 运行时。现在想把这些经验用到 Agent 基础设施上。

[noahgao.net](https://noahgao.net) · [github.com/noahziheng](https://github.com/noahziheng) · [noahgaocn@outlook.com](mailto:noahgaocn@outlook.com) · +86 186-0269-1005

## 工作经历

**字节跳动｜Dev Infra & MarsCode / Trae**（2021.9 – 至今）

- **云工作区基建**：主导基于容器二层调度的轻量化云工作区方案，把启动速度和资源占用压下来，支撑内部 CloudIDE 与对外的 MarsCode WebIDE，应对高弹性、性能突发、要求秒级就绪的场景<!-- TODO(Noah)：补一个真实数字，例如冷启时间 Xs→Ys、内存占用降低 Z%、支撑 N 个并发工作区 -->
- **Agent 运行时**：参与 Trae AI IDE 的 Agent 能力建设，用 Rust 近端 + Go 云端的架构支撑 Chat / Builder / SOLO 三条业务线，负责代码架构设计、网络层优化和自定义模型接入<!-- TODO(Noah)：可补日均会话数或工具调用次数 -->
- **开发框架**：参与开发并推广 Node.js 应用框架 Gulu 及其社区规范 Artus.js，主导 GuluX 重构版本，负责工具链服务端和数据统计
- **部署链路**：打通从工作区内构建到字节云、火山引擎、AWS 的托管 FaaS 发布流程

**阿里巴巴｜淘系技术部**（2019.7 – 2021.8）

- 负责天猫行业与轻店的业务前端，沉淀微前端一体化研发方案
- 推动业务在 FaaS / Serverless 上落地，建设业务域基础 Node 服务

## 个人探索

**Homelab：自己运维一套多可用区集群**
用 k3s 把天津家里的 NAS、北京海淀的 NUC 和两台腾讯云轻量服务器组成三可用区集群；配置用 Ansible 管、系统用 Nix 管、云资源用 Terraform 管、密钥用 SOPS 管，上面跑 Gitea、LobeChat、pgvector 等自用服务。目的是按生产环境的标准折腾自己的基础设施。

**Agent：把重复工作交给 Agent 编排**
自建了一套 Agent 编排体系（Hermes + Matrix + MCP + 定时任务），把运维巡检、联网检索、文档整理这类重复工作交给多个 Agent 协作完成。

**AGI：持续跟踪开源 Harness 实现**
研究 deepseek-harness、openclaw 等开源项目的源码，关注上下文管理、长期记忆、工具编排和自进化机制的具体做法。

## 技能

- **语言**：Go、Rust、Python、TypeScript / JavaScript
- **基础设施**：Linux、Docker、Kubernetes / k3s、Ansible、Terraform、Nix、SOPS、ArgoCD、CI/CD
- **其他**：FaaS / Serverless、Nginx、微前端

## 教育

天津科技大学 · 自动化 · 本科（工学学士）｜2015 – 2019

## 荣誉

字节跳动 Spot Bonus（2024 Q2）· 淘系技术部激情极客奖（2020）· 恩智浦杯全国大学生智能汽车竞赛二等奖（2018）
