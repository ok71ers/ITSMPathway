from crewai_tools import ScrapeWebsiteTool, SerperDevTool

from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task

@CrewBase
class ITSMBlogCrewTemplate:
    """ITSM Blog Creation crew template"""

    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    @agent
    def platform_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config["platform_analyst"],
            tools=[SerperDevTool(), ScrapeWebsiteTool()],
            allow_delegation=False,
            verbose=True,
        )

    @agent
    def content_strategist(self) -> Agent:
        return Agent(
            config=self.agents_config["content_strategist"],
            tools=[SerperDevTool(), ScrapeWebsiteTool()],
            allow_delegation=False,
            verbose=True,
        )

    @agent
    def technical_writer(self) -> Agent:
        return Agent(
            config=self.agents_config["technical_writer"],
            tools=[],
            allow_delegation=False,
            verbose=True,
        )

    @agent
    def seo_optimizer(self) -> Agent:
        return Agent(
            config=self.agents_config["seo_optimizer"],
            tools=[],
            allow_delegation=False,
            verbose=True,
        )

    @agent
    def editor(self) -> Agent:
        return Agent(
            config=self.agents_config["editor"],
            tools=[],
            allow_delegation=False,
            verbose=True,
        )

    @task
    def research_itsm_trends_task(self) -> Task:
        return Task(
            config=self.tasks_config["research_itsm_trends_task"],
            agent=self.platform_analyst(),
        )

    @task
    def develop_blog_outline_task(self) -> Task:
        return Task(
            config=self.tasks_config["develop_blog_outline_task"],
            agent=self.content_strategist(),
        )

    @task
    def write_blog_content_task(self) -> Task:
        return Task(
            config=self.tasks_config["write_blog_content_task"],
            agent=self.technical_writer(),
        )

    @task
    def optimize_blog_seo_task(self) -> Task:
        return Task(
            config=self.tasks_config["optimize_blog_seo_task"],
            agent=self.seo_optimizer(),
        )

    @task
    def final_review_and_edit_task(self) -> Task:
        return Task(
            config=self.tasks_config["final_review_and_edit_task"],
            agent=self.editor(),
            output_file="final_blog_post.md",
        )

    @crew
    def crew(self) -> Crew:
        """Creates the ITSM Blog Creation crew"""
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
        )