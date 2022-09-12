import os
import sys

class TablesManagement(object):
    def __init__(self, tables):
        self.currentPath = os.getcwd()
        self.tables = tables
        for table in self.tables:
            if not os.path.exists(table):
                os.mkdir(table)

    def generateRenameSqlScripts(self):
        for table in self.tables:
            generateRenameSqlScript(self, table)

    def generateRollBackSqlScripts(self):
        for table in self.tables:
            generateRollBackSqlScript(self, table)

    def generateDropSqlScripts(self):
        for table in self.tables:
            generateDropSqlScript(self, table)
            
    def generateRenameSqlScript(self, table):
        if os.path.exists(table):
            with open(os.path.join(table, 'rename.sql'), 'w') as sqlRenameTable:
                sqlRenameTable.write('RENAME ' + table + ' TO ' + 'drop_' + table + ';'

    def generateRollBackSqlScript(self, table):
        if os.path.exists(table):
            tableComponents = table.split('_');
            originalTable = tableComponents[len(tableComponents)-1]
            with open(os.path.join(table, 'rollback.sql'), 'w') as sqlRollBackTable:
                sqlRollBackTable.write('RENAME ' + table + ' TO ' + originalTable + ';';

    def generateDropSqlScript(self, table):
        if os.path.exists(table):
            with open(os.path.join(table, 'drop.sql'), 'w') as sqlDropTable:
                sqlDropTable.write('DROP TABLE ' + table + ';';

if __name__ == '__main__':
    args = sys.argv
    argTables = args.pop(0)
    tables = list(set(argTables))

    duplicatedTables = [table for table in argTables if table not in tables]
    print('The following duplicated tables have been filtered out: ')
    print(*duplicatedTables)

	tablesManagement = TablesManagement(tables)
	tablesManagement.generateRenameSqlScripts()
	tablesManagement.generateRollBackSqlScripts()
	tablesManagement.generateDropSqlScripts()
