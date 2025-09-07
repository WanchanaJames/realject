from fastapi import APIRouter, Depends
from models.users import ResponseSchema, TokenResponse, Register, Login
from sqlalchemy.orm import Session
from config import get_db
from passlib.context import CryptContext
from repository.users import UsersRepo, JWTRepo
from tables.users import Users

router = APIRouter(
    tags = {"Autherication"}
)

pwd_context = CryptContext(schemes = ['bcrypt'], deprecated = "auto")

#regis
@router.post('/signup')
async def signup(request: Register,db: Session = Depends(get_db)):
    try:
        #insert data
        _user = Users(        
            username = request.username,
            password = request.passwoed,
            email = request.email,
            phone_number = request.phone_number,
            first_name = request.first_name,
            last_name = request.last_name)
        UsersRepo.insert(db, _user)
        return ResponseSchema(code = "200", status = "Ok", message = "Success save data").dict(exclude_none = True)
    except Exception as error:
        print(error.args)
        return ReponseSchema(code = "500", status = "Error", message = "Internal Server Error").dict(exclude_none = True)
        
@router.post('/login')
async def login(request: Login, db: Session = Depends(get_db)):
    try:
        _user = UsersRepo.find_by_username(db, Users, request.username)

        if not pwd_context.verify(request.password, _user.password):
            return ReponseSchema(code = "400", status = "Bad Request", message = "Invalid password").dict(exclude_none = True)

        token = JWTRepo.generate_token({'sub': _user.username})
        return ReponseSchema(code = "200", status = "ok", message = "Seccess login", result = TokenResponse(access_token = token, token_type = "bearer").dict(exclude_none = True))
    
    except Exception as error:
        error_message = str(error.args)
        print(error_message)
        return ReponseSchema(code = "500", status = "Error", message = "Internal Server Error").dict(exclude_none = True)