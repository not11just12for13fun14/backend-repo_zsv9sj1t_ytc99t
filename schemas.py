"""
Database Schemas for Personal Website

Each Pydantic model maps to a MongoDB collection with the class name lowercased.
Example: class User -> collection "user"
"""

from pydantic import BaseModel, Field, EmailStr, HttpUrl
from typing import Optional, List

class Profile(BaseModel):
    full_name: str = Field(..., description="Full name of the person")
    title: str = Field(..., description="Short professional title")
    bio: str = Field(..., description="Short biography/about section")
    location: Optional[str] = Field(None, description="City, Country")
    email: Optional[EmailStr] = Field(None, description="Contact email")
    phone: Optional[str] = Field(None, description="Contact phone number")
    avatar_url: Optional[HttpUrl] = Field(None, description="Profile image URL")
    socials: Optional[dict] = Field(default_factory=dict, description="Map of social links: {platform: url}")

class Project(BaseModel):
    name: str = Field(..., description="Project name")
    description: str = Field(..., description="Short description")
    tech: List[str] = Field(default_factory=list, description="Technologies used")
    url: Optional[HttpUrl] = Field(None, description="Live URL")
    repo: Optional[HttpUrl] = Field(None, description="Repository URL")
    image_url: Optional[HttpUrl] = Field(None, description="Cover image URL")

class Experience(BaseModel):
    company: str = Field(..., description="Company/Organization name")
    role: str = Field(..., description="Role/Position title")
    start_date: str = Field(..., description="Start date, e.g., 2022-01")
    end_date: Optional[str] = Field(None, description="End date or 'Present'")
    description: Optional[str] = Field("", description="Highlights/Responsibilities")

class ContactMessage(BaseModel):
    name: str = Field(..., description="Sender name")
    email: EmailStr = Field(..., description="Sender email")
    message: str = Field(..., min_length=5, description="Message body")
