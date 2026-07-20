from typing import List
from pydantic import BaseModel, Field


class Candidate(BaseModel):
    name: str = ""
    email: str = ""
    phone: str = ""
    linkedin: str = ""
    github: str = ""


class Education(BaseModel):
    degree: str = ""
    institution: str = ""
    cgpa: str = ""
    year: str = ""


class Experience(BaseModel):
    company: str = ""
    role: str = ""
    duration: str = ""


class Project(BaseModel):
    name: str = ""
    description: str = ""
    technologies: List[str] = Field(default_factory=list)


class Skills(BaseModel):
    languages: List[str] = Field(default_factory=list)
    frameworks: List[str] = Field(default_factory=list)
    databases: List[str] = Field(default_factory=list)
    tools: List[str] = Field(default_factory=list)
    cloud: List[str] = Field(default_factory=list)
    ai_ml: List[str] = Field(default_factory=list)


class ResumeExtraction(BaseModel):
    candidate: Candidate = Field(default_factory=Candidate)
    education: List[Education] = Field(default_factory=list)
    experience: List[Experience] = Field(default_factory=list)
    projects: List[Project] = Field(default_factory=list)
    skills: Skills = Field(default_factory=Skills)
    certifications: List[str] = Field(default_factory=list)
    achievements: List[str] = Field(default_factory=list)