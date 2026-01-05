from dataclasses import dataclass

@dataclass
class user_Repository_DTO() :
    error : bool  = False
    msg : str = "success"