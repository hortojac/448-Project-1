/** -----------------------------------------------------------------------------
 *
 * @file  city.cpp
 * @author Julia Nichols 
 * Assignment:   EECS-268 Lab 7
 * @brief This file implements the functions created in city.h. It runs the main functionality of the program which consists of a "blob" that goes throughout the city and leaving it's mark where it is able to access.
 * @date 10/26/2021
 *
 ---------------------------------------------------------------------------- **/
#include "city.h"
#include <iostream>

City::City(std::ifstream& inFile)
{
    char temp;
    inFile >> m_rows >> m_cols >> m_start_x >> m_start_y;

    try
    {
        if(m_rows<1 || m_cols<1)
        {
            throw(std::runtime_error("ERROR: Number of rows/cols less than one.\n"));
        }
    }
    catch(std::runtime_error& e)
    {
        std::cout << e.what() << '\n';
    }
    try
    {
        if(m_start_x>(m_rows-1) || m_start_x<0 || m_start_y>(m_cols-1) || m_start_y<0)
        {
            throw(std::runtime_error("ERROR: Start position is out of range.\n"));
        }
    }
    catch(std::runtime_error& e)
    {
        std::cout << e.what() << '\n';
    }
    
    m_city = new char*[m_rows];
    for(int i=0; i<m_rows; i++)
    {
        m_city[i] = new char[m_cols];
    }
    for(int i=0; i<m_rows; i++)
    {
        for(int j=0; j<m_cols; j++)
        {
            inFile >> std::noskipws >> temp;
            if(temp!= '\n')
            {
                m_city[i][j] = temp;
            }
            else
            {
                inFile >> std::noskipws >> temp;
                m_city[i][j] = temp;
            }
        }
    }
}

void City::print()
{
    for(int i=0; i<m_rows; i++)
    {
        for(int j=0; j<m_cols; j++)
        {
            std::cout << m_city[i][j];
        }
        std::cout << "\n";
    }
}

void City::print2()
{
    for(int i=0; i<m_rows; i++)
    {
        for(int j=0; j<m_cols; j++)
        {
            std::cout << m_city[i][j];
        }
        std::cout << "\n";
    }
    std::cout << "\nTotal eaten: " << eaten << '\n';
}

City::~City()
{
    for(int i=0; i<m_rows; i++)
    {
        delete[] m_city[i];
    }
    delete[] m_city;
}

void City::blobbifyCity()
{
    blobbify(m_start_x, m_start_y);
}

void City::blobbify(int m_start_x, int m_start_y)
{
    if(m_city[m_start_x][m_start_y]=='S')
    {
        m_city[m_start_x][m_start_y] = 'B';
        if(m_start_y+1<=m_rows)
        {
            if(isValidMove(m_start_x, m_start_y+1))
            {
                blobbify(m_start_x, m_start_y+1);
            }
        }
        if(m_start_x+1<m_cols)
        {
            if(isValidMove(m_start_x+1, m_start_y))
            {
            blobbify(m_start_x+1, m_start_y);
            }
        }

        if(m_start_y-1>=0)
        {
            if(isValidMove(m_start_x, m_start_y-1))
            {
                blobbify(m_start_x, m_start_y-1);
            }
        }

        if(m_start_x-1>=0)
        {
            if(isValidMove(m_start_x-1, m_start_y))
            {
                blobbify(m_start_x-1, m_start_y);
            }
        }
    }

    else if(m_city[m_start_x][m_start_y]=='P')
    {
        eaten++;
        m_city[m_start_x][m_start_y] = 'B';
        if(m_start_y+1<=m_rows)
        {
            if(isValidMove(m_start_x, m_start_y+1))
            {
                blobbify(m_start_x, m_start_y+1);
            }
        }
        if(m_start_x+1<m_cols)
        {
            if(isValidMove(m_start_x+1, m_start_y))
            {
            blobbify(m_start_x+1, m_start_y);
            }
        }

        if(m_start_y-1>=0)
        {
            if(isValidMove(m_start_x, m_start_y-1))
            {
                blobbify(m_start_x, m_start_y-1);
            }
        }

        if(m_start_x-1>=0)
        {
            if(isValidMove(m_start_x-1, m_start_y))
            {
                blobbify(m_start_x-1, m_start_y);
            }
        }
    }
    else if(m_city[m_start_x][m_start_y]=='@')
    {
        for(int i=0; i<m_rows; i++)
        {
            for(int j=0; j<m_cols; j++)
            {
                if(m_city[i][j] == '@')
                {
                    blobbify(i, j+1);
                }
            }
        }
    }
    
}

bool City::isValidMove(int x, int y)
{
    if(m_city[x][y]=='P')
    {
        return true;
    }
    if(m_city[x][y]=='S')
    {
        return true;
    }
    if(m_city[x][y]=='#')
    {
        return false;
    }
    if(m_city[x][y]=='@')
    {
        return true;
    }
    if(m_city[x][y == 'B'])
    {
        return true;
    }
    else
    {
        return false;
    }
}
